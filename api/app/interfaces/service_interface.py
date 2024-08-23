from abc import ABC, abstractmethod

from app.schemas.diary_dto import DiaryDTO
from app.utils.result import Result


class DiaryServiceInterface(ABC):
    @abstractmethod
    def list_diaries(self) -> list[DiaryDTO]:
        pass

    @abstractmethod
    def get_diary_details(self, diary_id: str) -> DiaryDTO:
        pass

    @abstractmethod
    def add_new_diary(self, diary_data: DiaryDTO) -> Result:
        pass

    @abstractmethod
    def modify_diary(self, diary_id: str, diary_data: DiaryDTO) -> Result:
        pass

    @abstractmethod
    def remove_diary(self, diary_id: str) -> Result:
        pass
