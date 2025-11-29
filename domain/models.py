from datetime import timedelta

from openai import BaseModel


class TypeResponse(BaseModel):
    email_type: str
    important: int
    sla: timedelta


class EditResponse(BaseModel):
    result: str
    tokens: int


class AnswerResponse(BaseModel):
    result: str
    reply_to: list[str]
    tokens: int
