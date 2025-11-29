from openai import OpenAI

from domain.llmconfig import LLMConfig
from domain.models import EditResponse


class EditUsecase:
    def __init__(self, agent: OpenAI, config: LLMConfig) -> None:
        self._client = agent
        self._config = config

    def execute(self, text: str) -> EditResponse:
        res = self._client.responses.create(
            model=self._config.model,
            instructions=self._config.system_prompt,
            input=text,
            temperature=self._config.temperature,
            top_p=self._config.top_p,
            max_output_tokens=self._config.max_tokens,
        )
        return EditResponse(
            result=res.output_text,
            tokens=res.usage.total_tokens if res.usage else 0,
        )
