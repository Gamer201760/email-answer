from fastapi import Depends

from adapter.rest.settings import Settings, get_settings
from domain.llmconfig import LLMConfig
from repository.openai import OpenAILLMProvider
from usecase.answer import AnswerUsecase
from usecase.interface import LLMProviderRepository


def get_llm_config(
    settings: Settings = Depends(get_settings),
) -> LLMConfig:
    return LLMConfig(
        base_url='https://rest-assistant.api.cloud.yandex.net/v1',
        api_key=settings.api_key,
        model=f'gpt://{settings.folder_id}/qwen3-235b-a22b-fp8/latest',
        system_prompt=settings.base_prompt,
        folder_id=settings.folder_id,
    )


def get_llm_provider(
    config: LLMConfig = Depends(get_llm_config),
) -> LLMProviderRepository:
    return OpenAILLMProvider(config=config)


def get_answer_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent)


def get_edit_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
    settings: Settings = Depends(get_settings),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent.with_base_promt(settings.editing_prompt))


def get_type_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
    settings: Settings = Depends(get_settings),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent.with_base_promt(settings.type_prompt))
