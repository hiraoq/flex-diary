package com.flexdiary.controller

import com.flexdiary.model.DiaryEntry
import com.flexdiary.service.DiaryService
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/diary")
class DiaryController(private val diaryService: DiaryService) {

    @PostMapping("/{userId}")
    fun addDiaryEntry(@PathVariable userId: String, @RequestBody entryData: Map<String, Any>): DiaryEntry {
        return diaryService.addDiaryEntry(userId, entryData)
    }

    @GetMapping("/{userId}")
    fun getDiaryEntries(@PathVariable userId: String): List<DiaryEntry> {
        return diaryService.getDiaryEntries(userId)
    }

    @PutMapping("/{entryId}")
    fun updateDiaryEntry(@PathVariable entryId: String, @RequestBody updatedFields: Map<String, Any>): DiaryEntry? {
        return diaryService.updateDiaryEntry(entryId, updatedFields)
    }

    @DeleteMapping("/{entryId}")
    fun deleteDiaryEntry(@PathVariable entryId: String) {
        diaryService.deleteDiaryEntry(entryId)
    }

    @GetMapping("/hello")
    fun hello(): String {
        return "Hello, World!"
    }
}
