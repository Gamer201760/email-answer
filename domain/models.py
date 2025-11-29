from datetime import timedelta

from openai import BaseModel


class TypeResponse(BaseModel):
    letter_type: str
    importance: int
    sla: timedelta


class EditResponse(BaseModel):
    result: str
    tokens: int


class AnswerResponse(BaseModel):
    result: str
    reply_to: list[str]
    tokens: int
