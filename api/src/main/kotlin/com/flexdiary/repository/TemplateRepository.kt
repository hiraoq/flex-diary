package com.flexdiary.repository

import com.flexdiary.model.DiaryTemplate
import org.springframework.data.mongodb.repository.MongoRepository

interface TemplateRepository : MongoRepository<DiaryTemplate, String> {
    fun findByUserId(userId: String): DiaryTemplate?
    fun findByUserIdOrderByVersionDesc(userId: String): List<DiaryTemplate>
}
