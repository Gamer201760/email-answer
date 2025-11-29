from openai import BaseModel, OpenAI
from requests import Session

from domain.llmconfig import LLMConfig
from domain.models import AnswerResponse


class LAnswer(BaseModel):
    result: str
    depertament: str
    importance: int


class AnswerUsecase:
    def __init__(
        self,
        agent: OpenAI,
        config: LLMConfig,
        email_policy: dict[str, dict[str, list[str]]],
    ) -> None:
        self._client = agent
        self._config = config
        self._email_policy = email_policy
        self._session = Session()

    def execute(self, text: str) -> AnswerResponse | None:
        try:
            response = self._session.post(
                "http://localhost:8123/query", json={"query": text, "top_k": 3}
            )
            if response.status_code != 200:
                context = ""
            else:
                context = response.json()["context"]
        except Exception:
            context = ""

        dobavka = '\nЕще определи что это за департамент: Finance HR Marketing Sales Product Engineering и важность этого письма от 0 до 10, СТРОГО ФОРМАТ ОТВЕТА {"result": текст ответа, "depertament": департамент, "importance": важность [0, 10]}'

        res = self._client.responses.parse(
            text_format=LAnswer,
            model=self._config.model,
            instructions=self._config.system_prompt,
            input=context + text + dobavka,
            temperature=self._config.temperature,
            top_p=self._config.top_p,
            max_output_tokens=self._config.max_tokens,
        )
        if res.output_parsed:
            emails = []
            for i in range(res.output_parsed.importance):
                emails.extend(self._email_policy[res.output_parsed.depertament][str(i)])
            return AnswerResponse(
                result=res.output_parsed.result,
                tokens=res.usage.total_tokens if res.usage else 0,
                reply_to=emails,
            )
