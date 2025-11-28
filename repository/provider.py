class MockLLMProvider:
    def execute(self, text: str) -> tuple[str, int]:
        return text, 10
