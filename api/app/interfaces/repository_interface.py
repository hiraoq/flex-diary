from abc import ABC, abstractmethod

from app.schemas.diary_dto import DiaryDTO


class DiaryRepositoryInterface(ABC):
    @abstractmethod
    def get_all_diaries(self) -> list[DiaryDTO]:
        pass

    @abstractmethod
    def get_diary_by_id(self, diary_id: str) -> DiaryDTO | None:
        pass

    @abstractmethod
    def create_diary(self, diary_data: DiaryDTO) -> str:
        pass

    @abstractmethod
    def update_diary(self, diary_id: str, diary_data: DiaryDTO) -> int:
        pass

    @abstractmethod
    def delete_diary(self, diary_id: str) -> int:
        pass
