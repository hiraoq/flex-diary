package com.flexdiary

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class FlexDiaryApplication

fun main(args: Array<String>) {
	runApplication<FlexDiaryApplication>(*args)
}
