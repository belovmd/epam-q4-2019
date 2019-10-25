"""
Task from Checkio.
Print only uppercase letters
"""


def find_message(text: str) -> str:

    capital_letters = ""
    for letter in text:
        if letter.isupper():
            capital_letters += letter

    return capital_letters


print('Example:')
print(find_message("HELLOOOOOOO world!!!"))

assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
assert find_message("hello world!") == "", "Nothing"
assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
