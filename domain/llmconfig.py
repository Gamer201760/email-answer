from dataclasses import dataclass


@dataclass
class LLMConfig:
    api_key: str
    model: str
    base_url: str
    folder_id: str | None = None
    timeout: float = 10.0
    max_retries: int = 3

    temperature: float = 0.1
    top_p: float = 0.9
    max_tokens: int = 512

    system_prompt: str = ''
    response_format: str = 'text'
    language: str = 'ru-RU'

    tone: str = 'formal'
    max_reply_chars: int | None = None

    enable_safety_guardrails: bool = True
    security_prefix_prompt: str = ''

    def with_base_promt(self, base_promt: str) -> 'LLMConfig':
        self.system_prompt = base_promt
        return self
