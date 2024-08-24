import logging
import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from app.dependencies import get_database, get_mongo_client


class MainApp:
    def __init__(self) -> None:
        self.app = FastAPI(lifespan=self.lifespan)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        # 開発環境の場合にのみdebugpyを有効にする
        if os.getenv("FASTAPI_ENV") == "development":
            import debugpy

            self.logger.info("Starting debugpy...")
            debugpy.listen(("0.0.0.0", 5678))  # noqa: T100
            self.logger.info("Waiting for debugger to attach...")
            # 必要に応じて以下の行をコメントアウトまたは削除
            # debugpy.wait_for_client()  # noqa: ERA001
            self.logger.info("Debugger attached.")

    @asynccontextmanager
    async def lifespan(self, app: FastAPI) -> AsyncIterator[None]:
        self.logger.info("Starting up...")

        # dependencies.pyの設定を利用してMongoDBクライアントを取得
        client = get_mongo_client()
        db = get_database(client)

        # app.stateに保存
        app.state.mongodb_client = client
        app.state.mongodb = db
        self.logger.info("Connected to MongoDB!")

        yield

        self.logger.info("Shutting down...")
        if app.state.mongodb_client:
            app.state.mongodb_client.close()
        self.logger.info("MongoDB connection closed.")

    def include_routers(self) -> None:
        from app.routers import diary_router  # ルーターのインポート

        self.app.include_router(diary_router.router)

    def get_app(self) -> FastAPI:
        self.include_routers()
        return self.app


# MainAppを使用してアプリケーションを実行
main_app = MainApp()
app = main_app.get_app()
