package com.vega.app.premium

object SubscriptionManager {

    private var premium: Boolean = false

    fun update(status: Boolean) {
        premium = status
    }

    fun isPremium(): Boolean = premium
}
