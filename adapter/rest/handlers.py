from datetime import timedelta

from fastapi import APIRouter, Depends

from adapter.rest.di import get_answer_usecase, get_edit_usecase, get_type_usecase
from adapter.rest.models import (
    AnswerRequest,
    AnswerResponse,
    EditRequest,
    EditResponse,
    TypeResponse,
)
from usecase.answer import AnswerUsecase

router = APIRouter(prefix='/answers', tags=['answers'])


@router.post('/', response_model=AnswerResponse)
def create_answer(
    payload: AnswerRequest,
    usecase: AnswerUsecase = Depends(get_answer_usecase),
) -> AnswerResponse:
    result = usecase.execute(payload.text)
    return AnswerResponse(
        result=result[0], tokens=result[1], reply_to=[]
    )  # TODO: получать из usecase


@router.post('/edit', response_model=EditResponse)
def edit_answer(
    payload: EditRequest,
    usecase: AnswerUsecase = Depends(get_edit_usecase),
) -> EditResponse:
    result = usecase.execute(payload.text + payload.corrections)
    return EditResponse(result=result[0], tokens=result[1])


@router.post('/type', response_model=TypeResponse)
def get_type(
    payload: EditRequest,
    usecase: AnswerUsecase = Depends(get_type_usecase),
) -> TypeResponse:
    return TypeResponse(email_type='Info', sla=timedelta(days=2), important=1)
