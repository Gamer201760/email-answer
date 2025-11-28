from usecase.interface import LLMProviderRepository


class AnswerUsecase:
    def __init__(self, agent: LLMProviderRepository) -> None:
        self._signature_template = (
            ''  # Шаблон подписи, который всегда добавляется в конце
        )
        self._agent = agent

    def answer(self, text: str) -> tuple[str, int]:
        return self._agent.execute(text)

    def edit(self, text: str, corrections: str) -> tuple[str, int]:
        return self._agent.execute(text + corrections)
