from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_diary_service
from app.interfaces.service_interface import DiaryServiceInterface
from app.schemas.diary_dto import DiaryDTO
from app.schemas.diary_schema import (
    DiaryCreate,
    DiaryResponse,
    DiaryUpdate,
    MessageResponse,
)
from app.services.diary_service import DiaryService
from app.utils.converter import convert_diary_dto_to_response

if TYPE_CHECKING:
    from app.utils.result import Result

router = APIRouter()


# 疎通確認用エンドポイント
@router.get("/ping", response_model=str)
def ping() -> str:
    return "pong"


@router.get("/diaries/", response_model=list[DiaryResponse])
def list_diaries(
    service: DiaryServiceInterface = Depends(get_diary_service),
) -> list[DiaryResponse]:
    diaries = service.list_diaries()
    return [convert_diary_dto_to_response(diary) for diary in diaries]


@router.get("/diaries/{diary_id}", response_model=DiaryResponse)
def get_diary_details(
    diary_id: str,
    service: DiaryServiceInterface = Depends(get_diary_service),
) -> DiaryResponse:
    return convert_diary_dto_to_response(service.get_diary_details(diary_id))


@router.post("/diaries/", response_model=DiaryResponse)
def create_diary(
    diary_data: DiaryCreate,
    service: DiaryServiceInterface = Depends(get_diary_service),
) -> DiaryResponse:
    result: Result[DiaryDTO] = service.add_new_diary(DiaryDTO(**diary_data.dict()))
    if result.success and result.data is not None:
        return convert_diary_dto_to_response(result.data)
    raise HTTPException(status_code=400, detail=result.message)


@router.put("/diaries/{diary_id}", response_model=MessageResponse)
def update_diary(
    diary_id: str,
    diary_data: DiaryUpdate,
    service: DiaryServiceInterface = Depends(get_diary_service),
) -> MessageResponse:
    result = service.modify_diary(diary_id, DiaryDTO(**diary_data.dict()))
    if result.success:
        return MessageResponse(msg="Diary updated successfully")
    raise HTTPException(status_code=400, detail=result.message)


@router.delete("/diaries/{diary_id}", response_model=MessageResponse)
def delete_diary(
    diary_id: str,
    service: DiaryServiceInterface = Depends(get_diary_service),
) -> MessageResponse:
    result = service.remove_diary(diary_id)
    if result.success:
        return MessageResponse(msg="Diary deleted successfully")
    raise HTTPException(status_code=400, detail=result.message)
