package com.flexdiary.service

import com.flexdiary.model.DiaryEntry
import com.flexdiary.repository.DiaryRepository
import org.springframework.stereotype.Service

@Service
class DiaryService(
        private val diaryRepository: DiaryRepository,
        private val templateService: TemplateService
) {

    fun addDiaryEntry(userId: String, entryData: Map<String, Any>): DiaryEntry {
        val template = templateService.getLatestTemplate(userId)
        val entryFields = template?.fields ?: listOf()

        val entry = DiaryEntry(
                userId = userId,
                wakeUpTime = entryData["wakeUpTime"] as? String ?: "",
                exercise = entryData["exercise"] as? String,
                work = entryData["work"] as? String ?: "",
                focus = entryData["focus"] as? String ?: "",
                caloriesIntake = entryData["caloriesIntake"] as? Int,
                templateVersion = template?.version ?: 1
        )

        return diaryRepository.save(entry)
    }

    fun getDiaryEntries(userId: String): List<DiaryEntry> {
        return diaryRepository.findByUserId(userId)
    }

    fun updateDiaryEntry(entryId: String, updatedFields: Map<String, Any>): DiaryEntry? {
        val entry = diaryRepository.findById(entryId).orElse(null) ?: return null
        updatedFields.forEach { (key, value) ->
            val field = DiaryEntry::class.java.getDeclaredField(key)
            field.isAccessible = true
            field.set(entry, value)
        }
        return diaryRepository.save(entry)
    }

    fun deleteDiaryEntry(entryId: String) {
        diaryRepository.deleteById(entryId)
    }
}