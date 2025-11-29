from datetime import timedelta

from openai import BaseModel, OpenAI

from domain.llmconfig import LLMConfig
from domain.models import TypeResponse


class LType(BaseModel):
    letter_type: str
    importance: int


class GetTypeUsecase:
    def __init__(self, agent: OpenAI, config: LLMConfig) -> None:
        self._client = agent
        self._config = config

    def execute(self, text: str) -> TypeResponse | None:
        res = self._client.responses.parse(
            text_format=LType,
            model=self._config.model,
            instructions=self._config.system_prompt,
            input=text,
            temperature=self._config.temperature,
            top_p=self._config.top_p,
            max_output_tokens=self._config.max_tokens,
        )
        if res.output_parsed:
            return TypeResponse(
                letter_type=res.output_parsed.letter_type,
                importance=res.output_parsed.importance,
                sla=timedelta(days=1),
            )
