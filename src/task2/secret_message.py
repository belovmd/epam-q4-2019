"""Gather all capital letters in one word in the order."""


def find_message(text: str) -> str:
    message = ""
    for i in text:
        if i.isupper():
            message += i
    return message


print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
