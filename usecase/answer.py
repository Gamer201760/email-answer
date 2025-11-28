from usecase.interface import LLMProviderRepository


class AnswerUsecase:
    def __init__(
        self,
        agent: LLMProviderRepository,
    ) -> None:
        self._agent = agent

    def execute(self, text: str) -> tuple[str, int]:
        return self._agent.execute(text)
