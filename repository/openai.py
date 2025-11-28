from openai import OpenAI

from domain.llmconfig import LLMConfig


class OpenAILLMProvider:
    def __init__(self, config: LLMConfig) -> None:
        self._config = config
        self._client = OpenAI(
            base_url=self._config.base_url,
            api_key=self._config.api_key,
            project=self._config.folder_id,
        )

    def execute(self, text: str) -> tuple[str, int]:
        res = self._client.responses.create(
            model=self._config.model,
            instructions=self._config.system_prompt,
            input=text,
            temperature=self._config.temperature,
            top_p=self._config.top_p,
            max_output_tokens=self._config.max_tokens,
        )
        return res.output_text, res.usage.total_tokens if res.usage else 0

    def with_base_promt(self, base_promt: str) -> 'OpenAILLMProvider':
        self._config.system_prompt = base_promt
        return self
