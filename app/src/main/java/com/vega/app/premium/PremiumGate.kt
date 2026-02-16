package com.vega.app.premium

object PremiumGate {

    fun requirePremium(action: () -> Unit) {
        if (SubscriptionManager.isPremium()) action()
        else throw IllegalAccessException("Premium Required")
    }
}
