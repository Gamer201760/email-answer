from functools import lru_cache

from fastapi import Path
from pydantic import Field
from pydantic_settings import BaseSettings

BASE_PROMPT_PATH = Path('promt/system.txt')


def load_base_prompt() -> str:
    return BASE_PROMPT_PATH.read_text(encoding='utf-8')


class Settings(BaseSettings):
    port: int
    host: str
    dev: bool
    api_key: str
    folder_id: str

    base_prompt: str = Field(default_factory=load_base_prompt)

    class Config:
        env_file = '.env'


@lru_cache
def get_settings() -> Settings:
    return Settings()
