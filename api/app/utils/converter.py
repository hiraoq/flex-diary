from app.schemas.diary_dto import DiaryDTO, DiaryEntryDTO
from app.schemas.diary_schema import DiaryEntry, DiaryResponse


def convert_diary_dto_to_response(diary_dto: DiaryDTO) -> DiaryResponse:
    entries = [DiaryEntry(**entry.dict()) for entry in diary_dto.entries]
    return DiaryResponse(
        diary_id=diary_dto.diary_id,
        template_id=diary_dto.template_id,
        date=diary_dto.date,
        entries=entries,
        metadata=diary_dto.metadata,
    )
