from openai import BaseModel


class TypeResponse(BaseModel):
    letter_type: str
    importance: int
    sla: int


class EditResponse(BaseModel):
    result: str
    tokens: int


class AnswerResponse(BaseModel):
    result: str
    reply_to: list[str]
    tokens: int
