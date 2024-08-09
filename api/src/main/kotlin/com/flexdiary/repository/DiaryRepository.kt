package com.flexdiary.repository

import com.flexdiary.model.DiaryEntry
import org.springframework.data.mongodb.repository.MongoRepository

interface DiaryRepository : MongoRepository<DiaryEntry, String> {
    fun findByUserId(userId: String): List<DiaryEntry>
}
