def find_message(text: str) -> str:
    """Gather all capital letters in one word in the order that

    they appear in the text.
    """
    line = ""
    for ch in text:
        if ch.isupper():
            line += ch
    return line
