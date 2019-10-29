"""Gather all capital letters in one word in the order."""


def find_message(text: str) -> str:
    find_message = ""
    for i in text:
        if i.isupper():
            find_message += i
    return find_message


if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))

    assert "HELLO" == \
           find_message("How are you? Eh, ok. Low or Lower? Ohhh."), "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
