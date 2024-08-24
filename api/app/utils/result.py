from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Result(Generic[T]):
    def __init__(
        self,
        success: bool,  # noqa: FBT001
        data: T | None = None,
        message: str | None = None,
    ) -> None:
        self.success = success
        self.data = data
        self.message = message
