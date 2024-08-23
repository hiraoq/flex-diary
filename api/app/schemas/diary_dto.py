from datetime import datetime

from pydantic import BaseModel


class DiaryEntryDTO(BaseModel):
    field_id: str
    value: str


class DiaryDTO(BaseModel):
    diary_id: str | None = None
    template_id: str
    date: datetime
    entries: list[DiaryEntryDTO]
    metadata: dict | None = None
