from usecase.interface import LLMProviderRepository


class AnswerUsecase:
    def __init__(
        self,
        agent: LLMProviderRepository,
        correcting: LLMProviderRepository,
    ) -> None:
        self._agent = agent
        self._correcting = correcting

    def answer(self, text: str) -> tuple[str, int]:
        return self._agent.execute(text)

    def edit(self, text: str, corrections: str) -> tuple[str, int]:
        return self._correcting.execute(text + corrections)

    def get_type(self,):
        pass
