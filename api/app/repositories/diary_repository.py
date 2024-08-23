from bson import ObjectId
from pymongo import database

from app.interfaces.repository_interface import DiaryRepositoryInterface
from app.schemas.diary_dto import DiaryDTO


class DiaryRepository(DiaryRepositoryInterface):
    def __init__(self, db_client: database.Database) -> None:
        self.db_client = db_client

    def get_all_diaries(self) -> list[DiaryDTO]:
        diaries = self.db_client.diaries.find({})
        return [DiaryDTO(**diary) for diary in diaries]

    def get_diary_by_id(self, diary_id: str) -> DiaryDTO | None:
        diary = self.db_client.diaries.find_one(
            {"_id": ObjectId(diary_id)},
        )
        if diary:
            return DiaryDTO(**diary)
        return None

    def create_diary(self, diary_data: DiaryDTO) -> str:
        # Pydanticモデルを辞書に変換
        diary_dict = diary_data.dict()

        # 辞書形式のデータをMongoDBに挿入
        result = self.db_client.diaries.insert_one(diary_dict)

        # 挿入されたドキュメントのIDを返す
        return str(result.inserted_id)

    def update_diary(self, diary_id: str, diary_data: DiaryDTO) -> int:
        result = self.db_client.diaries.update_one(
            {"_id": ObjectId(diary_id)},
            {"$set": diary_data},
        )
        return result.modified_count

    def delete_diary(self, diary_id: str) -> int:
        result = self.db_client.diaries.delete_one({"_id": ObjectId(diary_id)})
        return result.deleted_count
