from usecase.interface import LLMProviderRepository


class AnswerUsecase:
    def __init__(
        self,
        agent: LLMProviderRepository,
        system_promt: str,
    ) -> None:
        self._agent = agent.with_base_promt(system_promt)

    def execute(self, text: str) -> tuple[str, int]:
        return self._agent.execute(text)
