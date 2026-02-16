package com.vega.app

import android.os.Bundle
import android.webkit.WebView
import androidx.appcompat.app.AppCompatActivity
import com.vega.app.core.AppConfig
import com.vega.app.security.SecurityManager

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        if (!SecurityManager.validateEnvironment()) {
            finish()
        }

        webView = WebView(this)
        webView.settings.javaScriptEnabled = false
        webView.loadUrl("file:///android_asset/index.html")

        setContentView(webView)
    }
}
