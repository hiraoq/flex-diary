from collections.abc import Callable

from pymongo.errors import OperationFailure, WriteError

from app.interfaces.repository_interface import DiaryRepositoryInterface
from app.interfaces.service_interface import DiaryServiceInterface
from app.schemas.diary_dto import DiaryDTO
from app.utils.exceptions import DiaryNotFoundError
from app.utils.handler import handle_db_exceptions
from app.utils.result import Result


class DiaryService(DiaryServiceInterface):
    def __init__(self, diary_repository: DiaryRepositoryInterface) -> None:
        self.diary_repository = diary_repository

    def list_diaries(self) -> list[DiaryDTO]:
        return self.diary_repository.get_all_diaries()

    def get_diary_details(self, diary_id: str) -> DiaryDTO:
        diary = self.diary_repository.get_diary_by_id(diary_id)
        if diary is None:
            raise DiaryNotFoundError(diary_id)
        return diary

    def add_new_diary(self, diary_data: DiaryDTO) -> Result:
        result = handle_db_exceptions(
            lambda: self.diary_repository.create_diary(diary_data),
        )
        # ここでDiaryDTOを取得し直す
        new_diary_data = self.diary_repository.get_diary_by_id(result.data)
        return Result(success=True, data=new_diary_data)

    def modify_diary(self, diary_id: str, diary_data: DiaryDTO) -> Result:
        return handle_db_exceptions(
            lambda: self.diary_repository.update_diary(diary_id, diary_data),
        )

    def remove_diary(self, diary_id: str) -> Result:
        return handle_db_exceptions(
            lambda: self.diary_repository.delete_diary(diary_id),
        )
