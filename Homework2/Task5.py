"""
Task from Checkio.
returns the first word in a given text.
"""


def first_word(text: str) -> str:
    text = text + " "
    word = ""
    f = False
    not_letters = " !.,?:\\/"

    for symbol in text:
        if symbol in not_letters:
            if f:
                return word
            else:
                word = ""
        else:
            word += symbol
            f = True

    return "There is no words"

print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
