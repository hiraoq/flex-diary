package com.flexdiary.model

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document
import java.time.LocalDateTime

@Document(collection = "templates")
data class DiaryTemplate(
        @Id val id: String? = null,
        val userId: String,
        val fields: List<String>,
        val version: Int,
        val createdAt: LocalDateTime = LocalDateTime.now()
)
