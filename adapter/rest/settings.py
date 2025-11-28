from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: int
    host: str
    dev: bool
    api_key: str
    folder_id: str

    class Config:
        env_file = '.env'


@lru_cache
def get_settings() -> Settings:
    return Settings()
