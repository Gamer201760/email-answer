from domain.llmconfig import LLMConfig


class MockLLMProvider:
    def __init__(self, config: LLMConfig) -> None:
        pass

    def execute(self, text: str) -> tuple[str, int]:
        return text, 10
