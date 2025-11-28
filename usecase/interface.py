from typing import Protocol

from domain.llmconfig import LLMConfig


class LLMProviderRepository(Protocol):
    def __init__(self, config: LLMConfig) -> None: ...
    def execute(self, text: str) -> tuple[str, int]:
        "tuple[ответ, кол-во потраченных токенов]"
        ...
