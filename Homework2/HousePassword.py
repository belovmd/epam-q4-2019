"""
Stephan and Sophia forget about security and use simple passwords
for everything. Help Nikola develop a password security check module.
The password will be considered strong enough if its length is greater
than or equal to 10 symbols, it has at least one digit, as well as
containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type
that can be converted and processed as a boolean.
In the results you will see the converted results.
"""
import re


def checkio(data: str) -> bool:
    digit = r"\d"
    upper = r"[A-Z]"
    lower = r"[a-z]"
    if len(data) < 10:
        return False
    elif not re.findall(digit, data):
        return False
    elif not re.findall(upper, data):
        return False
    elif not re.findall(lower, data):
        return False
    return True


if __name__ == '__main__':
    print(checkio("ULFFunH8ni"))
