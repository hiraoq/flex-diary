package com.flexdiary.model

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document
import java.time.LocalDateTime

@Document(collection = "diaries")
data class DiaryEntry(
        @Id val id: String? = null,
        val userId: String,
        val date: LocalDateTime = LocalDateTime.now(),
        val wakeUpTime: String,
        val exercise: String?,
        val work: String,
        val focus: String,
        val caloriesIntake: Int?,
        val templateVersion: Int
)