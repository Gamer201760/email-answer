from pydantic import BaseModel


class AnswerRequest(BaseModel):
    text: str
    email_type: str


class EditRequest(BaseModel):
    text: str
    corrections: str
