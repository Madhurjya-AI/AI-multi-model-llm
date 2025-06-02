def classify_task(user_input: str) -> str:
    if any(kw in user_input.lower() for kw in ["write a function", "python code", "bug", "fix", "loop", "algorithm"]):
        return "code"
    return "chat"