PARTNERSHIP_TERMS = [
    "joint venture",
    "strategic partnership",
    "collaboration",
    "alliance",
    "consortium"
]


def detect_partnership(text):
    text = text.lower()

    for t in PARTNERSHIP_TERMS:
        if t in text:
            return True

    return False
