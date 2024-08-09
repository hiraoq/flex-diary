package com.flexdiary.controller

import com.flexdiary.model.DiaryTemplate
import com.flexdiary.service.TemplateService
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/template")
class TemplateController(private val templateService: TemplateService) {

    @PostMapping("/{userId}")
    fun addOrUpdateTemplate(@PathVariable userId: String, @RequestBody fields: List<String>): DiaryTemplate {
        return templateService.addOrUpdateTemplate(userId, fields)
    }

    @GetMapping("/{userId}")
    fun getLatestTemplate(@PathVariable userId: String): DiaryTemplate? {
        return templateService.getLatestTemplate(userId)
    }

    @GetMapping("/{userId}/version/{version}")
    fun getTemplateByVersion(@PathVariable userId: String, @PathVariable version: Int): DiaryTemplate? {
        return templateService.getTemplateByVersion(userId, version)
    }

    @GetMapping("/{userId}/history")
    fun getAllTemplates(@PathVariable userId: String): List<DiaryTemplate> {
        return templateService.getAllTemplates(userId)
    }
}
