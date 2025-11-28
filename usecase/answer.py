from usecase.interface import LLMProviderRepository


class AnswerUsecase:
    def __init__(self, agent: LLMProviderRepository) -> None:
        self._base_promt = ''
        self._agent = agent

    def answer(self, text: str) -> str: ...
    def edit(self, text: str, corrections: str) -> str: ...
