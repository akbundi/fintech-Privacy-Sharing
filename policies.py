POLICIES = {
    "credit_score_api": ["income", "transaction_history"],
    "investment_advisor": ["income", "name"],
    "analytics_partner": ["transaction_history", "device_data"]
}

def get_allowed_fields(requester):
    return POLICIES.get(requester, [])
