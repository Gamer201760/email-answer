from datetime import timedelta

from pydantic import BaseModel


class AnswerRequest(BaseModel):
    text: str
    email_type: str


class EditRequest(BaseModel):
    text: str
    corrections: str


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
