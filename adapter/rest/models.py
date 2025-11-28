from pydantic import BaseModel


class AnswerRequest(BaseModel):
    text: str


class EditRequest(BaseModel):
    text: str
    corrections: str


class AnswerResponse(BaseModel):
    result: str
    tokens: int
