from collections.abc import Callable
from typing import Optional

from pymongo.errors import DuplicateKeyError, OperationFailure

from app.utils.result import Result


def handle_db_exceptions(operation: Callable[..., object]) -> "Result":
    try:
        result = operation()
        return Result(success=True, data=result)
    except DuplicateKeyError:
        return Result(success=False, message="Diary with the same ID already exists.")
    except TypeError:
        return Result(success=False, message="Invalid data type provided.")
    except ValueError:
        return Result(success=False, message="Invalid value provided.")
    except OperationFailure as e:
        return Result(success=False, message=f"Database operation failed: {e}")
    except Exception as e:  # noqa: BLE001
        return Result(success=False, message=f"Unexpected error: {e}")
