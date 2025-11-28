class LLMProviderRepository:
    def execute(self, text: str) -> tuple[str, int]:
        "tuple[ответ, кол-во потраченных токенов]"
        ...
