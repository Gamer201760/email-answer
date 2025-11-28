from fastapi import Depends

from repository.provider import MockLLMProvider
from usecase.answer import AnswerUsecase
from usecase.interface import LLMProviderRepository


def get_llm_provider() -> LLMProviderRepository:
    return MockLLMProvider()


def get_answer_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent)
