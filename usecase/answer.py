from openai import OpenAI

from domain.llmconfig import LLMConfig
from domain.models import AnswerResponse


class AnswerUsecase:
    def __init__(self, agent: OpenAI, config: LLMConfig) -> None:
        self._client = agent
        self._config = config

    def execute(self, text: str) -> AnswerResponse:
        res = self._client.responses.create(
            model=self._config.model,
            instructions=self._config.system_prompt,
            input=text,
            temperature=self._config.temperature,
            top_p=self._config.top_p,
            max_output_tokens=self._config.max_tokens,
        )
        return AnswerResponse(
            result=res.output_text,
            tokens=res.usage.total_tokens if res.usage else 0,
            reply_to=['azamat201760@ya.ru'],
        )
