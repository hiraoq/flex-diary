from fastapi import Depends
from pymongo import MongoClient
from pymongo.database import Database

from app.interfaces.repository_interface import DiaryRepositoryInterface
from app.interfaces.service_interface import DiaryServiceInterface
from app.repositories.diary_repository import DiaryRepository
from app.services.diary_service import DiaryService


# 同期MongoDBクライアントを取得する関数 TODO: 非同期化
def get_mongo_client() -> MongoClient:
    return MongoClient("mongodb://root:example@mongodb:27017")


# データベースを取得する関数 TODO: 非同期化
def get_database(
    client: MongoClient = Depends(get_mongo_client),
) -> Database:
    return client["flex-diary"]


# リポジトリの依存関係を提供する関数
def get_diary_repository(
    db: Database = Depends(get_database),
) -> DiaryRepositoryInterface:
    return DiaryRepository(db)


# サービスの依存関係を提供する関数
def get_diary_service(
    repository: DiaryRepositoryInterface = Depends(get_diary_repository),
) -> DiaryServiceInterface:
    return DiaryService(repository)
