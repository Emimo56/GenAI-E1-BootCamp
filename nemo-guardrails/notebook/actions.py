from nemoguardrails.actions import action

@action()
def is_sensitive_topic(input_text: str):
    banned = ["password", "credit card"]
    return any(word in input_text.lower() for word in banned)