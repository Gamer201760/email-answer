from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


def load_base_prompt() -> str:
    with open('promt/system.txt') as f:
        return f.read().strip()


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
