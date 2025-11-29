from fastapi import Depends
from openai import OpenAI

from adapter.rest.settings import Settings, get_settings
from domain.llmconfig import LLMConfig
from usecase.answer import AnswerUsecase
from usecase.edit import EditUsecase
from usecase.get_type import GetTypeUsecase


def get_llm_config(
    settings: Settings = Depends(get_settings),
) -> LLMConfig:
    return LLMConfig(
        base_url="https://rest-assistant.api.cloud.yandex.net/v1",
        api_key=settings.api_key,
        model=f"gpt://{settings.folder_id}/qwen3-235b-a22b-fp8/latest",
        system_prompt=settings.base_prompt,
        folder_id=settings.folder_id,
    )


def get_openai(
    config: LLMConfig = Depends(get_llm_config),
) -> OpenAI:
    return OpenAI(
        base_url=config.base_url,
        api_key=config.api_key,
        project=config.folder_id,
    )


def get_answer_usecase(
    agent: OpenAI = Depends(get_openai),
    config: LLMConfig = Depends(get_llm_config),
    settings: Settings = Depends(get_settings),
) -> AnswerUsecase:
    return AnswerUsecase(agent, config.with_base_promt(settings.base_prompt))


def get_edit_usecase(
    agent: OpenAI = Depends(get_openai),
    config: LLMConfig = Depends(get_llm_config),
    settings: Settings = Depends(get_settings),
) -> EditUsecase:
    return EditUsecase(
        agent, config.with_base_promt(settings.base_prompt + settings.editing_prompt)
    )


def get_type_usecase(
    agent: OpenAI = Depends(get_openai),
    config: LLMConfig = Depends(get_llm_config),
    settings: Settings = Depends(get_settings),
) -> GetTypeUsecase:
    return GetTypeUsecase(
        agent,
        config.with_base_promt(settings.base_prompt + settings.type_prompt),
        settings.sla_policy,
    )
