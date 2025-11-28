from typing import Protocol


class LLMProviderRepository(Protocol):
    def execute(self, text: str) -> tuple[str, int]:
        "tuple[ответ, кол-во потраченных токенов]"
        ...
