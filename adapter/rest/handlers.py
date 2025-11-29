from fastapi import APIRouter, Depends

from adapter.rest.di import get_answer_usecase, get_edit_usecase, get_type_usecase
from adapter.rest.models import (
    AnswerRequest,
    EditRequest,
    TypeRequest,
)
from domain.models import AnswerResponse, EditResponse, TypeResponse
from usecase.answer import AnswerUsecase
from usecase.edit import EditUsecase
from usecase.get_type import GetTypeUsecase

router = APIRouter(prefix='/answers', tags=['answers'])


@router.post('/', response_model=AnswerResponse)
def create_answer(
    payload: AnswerRequest,
    usecase: AnswerUsecase = Depends(get_answer_usecase),
) -> AnswerResponse:
    return usecase.execute(payload.text)


@router.post('/edit', response_model=EditResponse)
def edit_answer(
    payload: EditRequest,
    usecase: EditUsecase = Depends(get_edit_usecase),
) -> EditResponse:
    return usecase.execute(payload.text + payload.corrections)


@router.post('/type', response_model=TypeResponse)
def get_type(
    payload: TypeRequest,
    usecase: GetTypeUsecase = Depends(get_type_usecase),
) -> TypeResponse | None:
    return usecase.execute(payload.text)
