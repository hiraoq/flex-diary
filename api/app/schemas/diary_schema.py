# schemas/diary_schema.py

from datetime import datetime

from pydantic import BaseModel


class DiaryEntry(BaseModel):
    field_id: str
    value: str


class DiaryCreate(BaseModel):
    template_id: str
    date: datetime
    entries: list[DiaryEntry]
    metadata: dict | None = None


class DiaryUpdate(BaseModel):
    entries: list[DiaryEntry] | None = None
    metadata: dict | None = None


class DiaryResponse(BaseModel):
    diary_id: str
    template_id: str
    date: datetime
    entries: list[DiaryEntry]
    metadata: dict | None = None


class MessageResponse(BaseModel):
    msg: str
