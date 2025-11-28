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


def get_correcting_provider(
    config: LLMConfig = Depends(get_llm_config),
    settings: Settings = Depends(get_settings),
) -> LLMProviderRepository:
    config.system_prompt = settings.editing_prompt
    return OpenAILLMProvider(config=config)


def get_answer_usecase(
    agent: LLMProviderRepository = Depends(get_llm_provider),
    correcting: LLMProviderRepository = Depends(get_correcting_provider),
) -> AnswerUsecase:
    return AnswerUsecase(agent=agent, correcting=correcting)
