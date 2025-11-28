from fastapi import APIRouter, Depends

from adapter.rest.di import get_answer_usecase, get_edit_usecase, get_type_usecase
from adapter.rest.models import AnswerRequest, AnswerResponse, EditRequest
from usecase.answer import AnswerUsecase

router = APIRouter(prefix='/answers', tags=['answers'])


@router.post('/', response_model=AnswerResponse)
def create_answer(
    payload: AnswerRequest,
    usecase: AnswerUsecase = Depends(get_answer_usecase),
) -> AnswerResponse:
    result = usecase.execute(payload.text)
    return AnswerResponse(result=result[0], tokens=result[1])


@router.post('/edit', response_model=AnswerResponse)
def edit_answer(
    payload: EditRequest,
    usecase: AnswerUsecase = Depends(get_edit_usecase),
) -> AnswerResponse:
    result = usecase.execute(payload.text + payload.corrections)
    return AnswerResponse(result=result[0], tokens=result[1])


@router.post('/type', response_model=AnswerResponse)
def get_type(
    payload: EditRequest,
    usecase: AnswerUsecase = Depends(get_type_usecase),
) -> AnswerResponse:
    result = usecase.execute(payload.text)
    return AnswerResponse(result=result[0], tokens=result[1])
