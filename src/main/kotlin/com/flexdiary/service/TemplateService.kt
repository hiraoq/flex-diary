package com.flexdiary.service

import com.flexdiary.model.DiaryTemplate
import com.flexdiary.repository.TemplateRepository
import org.springframework.stereotype.Service

@Service
class TemplateService(private val templateRepository: TemplateRepository) {

    fun addOrUpdateTemplate(userId: String, fields: List<String>): DiaryTemplate {
        val templates = templateRepository.findByUserIdOrderByVersionDesc(userId)
        val newVersion = if (templates.isNotEmpty()) templates.first().version + 1 else 1
        val newTemplate = DiaryTemplate(userId = userId, fields = fields, version = newVersion)
        return templateRepository.save(newTemplate)
    }

    fun getLatestTemplate(userId: String): DiaryTemplate? {
        return templateRepository.findByUserIdOrderByVersionDesc(userId).firstOrNull()
    }

    fun getTemplateByVersion(userId: String, version: Int): DiaryTemplate? {
        return templateRepository.findByUserIdOrderByVersionDesc(userId).find { it.version == version }
    }

    fun getAllTemplates(userId: String): List<DiaryTemplate> {
        return templateRepository.findByUserIdOrderByVersionDesc(userId)
    }
}
