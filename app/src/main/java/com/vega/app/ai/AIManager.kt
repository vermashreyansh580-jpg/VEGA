package com.vega.app.ai

import com.vega.app.core.Result
import okhttp3.*

class AIManager(private val apiKey: String) {

    private val client = OkHttpClient()

    fun ask(prompt: String, callback: (Result<String>) -> Unit) {

        val json = """
            {
              "model": "llama3-8b-8192",
              "messages": [{"role":"user","content":"$prompt"}]
            }
        """.trimIndent()

        val request = Request.Builder()
            .url("https://api.groq.com/openai/v1/chat/completions")
            .addHeader("Authorization", "Bearer $apiKey")
            .post(RequestBody.create(
                "application/json".toMediaTypeOrNull(), json))
            .build()

        client.newCall(request).enqueue(object: Callback {
            override fun onFailure(call: Call, e: IOException) {
                callback(Result.Error(e.message ?: "Error"))
            }

            override fun onResponse(call: Call, response: Response) {
                callback(Result.Success(response.body?.string() ?: ""))
            }
        })
    }
}
