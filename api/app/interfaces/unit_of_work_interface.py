from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import types


# トランザクション管理が必要であれば使用する。
# トランザクション管理が必要ない場合、このinterfaceは不要。
class UnitOfWorkInterface(ABC):
    @abstractmethod
    def __enter__(self) -> UnitOfWorkInterface:
        pass

    @abstractmethod
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass
