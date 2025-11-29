import json
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


def load_base_prompt() -> str:
    with open("promt/system.txt") as f:
        return f.read().strip()


def load_editing_prompt() -> str:
    with open("promt/grinding.txt") as f:
        return f.read().strip()


def load_type_prompt() -> str:
    with open("promt/get_type.txt") as f:
        return f.read().strip()


def load_sla_policy() -> dict[str, int]:
    with open("policy/sla.json") as f:
        return json.load(f)


class Settings(BaseSettings):
    port: int
    host: str
    dev: bool
    api_key: str
    folder_id: str

    base_prompt: str = Field(default_factory=load_base_prompt)
    editing_prompt: str = Field(default_factory=load_editing_prompt)
    type_prompt: str = Field(default_factory=load_type_prompt)

    sla_policy: dict[str, int] = Field(default_factory=load_sla_policy)

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()
