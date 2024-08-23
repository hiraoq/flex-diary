# utils/exceptions.py


class DiaryNotFoundError(Exception):
    """
    指定されたIDの日記エントリーが見つからない場合に発生します。
    """

    def __init__(self, diary_id: str) -> None:
        message = f"ID '{diary_id}' の日記が見つかりませんでした"
        super().__init__(message)
        self.diary_id = diary_id


class InvalidDiaryDataError(Exception):
    """
    提供された日記データが無効である場合に発生します。
    """

    def __init__(self, reason: str) -> None:
        message = f"無効な日記データ: {reason}"
        super().__init__(message)
        self.reason = reason


class DatabaseConnectionError(Exception):
    """
    データベース接続に問題がある場合に発生します。
    """

    def __init__(self, db_name: str, error: str) -> None:
        message = f"データベース '{db_name}' への接続エラー: {error}"
        super().__init__(message)
        self.db_name = db_name
        self.error = error
