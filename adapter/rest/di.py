from fastapi import Depends

from adapter.rest.settings import Settings, get_settings
from domain.llmconfig import LLMConfig
from repository.openrouter_provider import OpenRouterLLMProvider
from repository.provider import MockLLMProvider
from usecase.answer import AnswerUsecase
from usecase.interface import LLMProviderRepository


def get_system_promt() -> str:
    with open('promt/system.txt') as f:
        return f.read()


def get_llm_config(
    promt: str = Depends(get_system_promt),
    settings: Settings = Depends(get_settings),
) -> LLMConfig:
    return LLMConfig(
        api_key=settings.llm_api_key,  # Из env
        model='google/gemma-3n-e4b-it:free',
        system_prompt=promt,  # Подгружаем из txt
    )


def get_llm_provider(
    config: LLMConfig = Depends(get_llm_config),
) -> LLMProviderRepository:
    return OpenRouterLLMProvider(config=config)
    return MockLLMProvider(config=config)


def get_answer_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent)
