package com.flexdiary.controller

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api")
class DiaryController {

    @GetMapping("/hello")
    fun hello(): String {
        return "Hello, World!"
    }
}