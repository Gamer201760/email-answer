from fastapi import Depends

from adapter.rest.settings import Settings, get_settings
from domain.llmconfig import LLMConfig
from repository.openai import OpenAILLMProvider
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
        base_url='https://rest-assistant.api.cloud.yandex.net/v1',
        api_key=settings.api_key,
        model=f'gpt://{settings.folder_id}/qwen3-235b-a22b-fp8/latest',
        system_prompt=promt,
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
