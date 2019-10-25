"""
Task from Checkio.
Check if string length >= 10 and it has at least one uppercase letter,
one lowercase letter and one digit
"""
import re


def checkio(data: str) -> bool:
    if not bool(re.search("[A-Z]", data)):
        return False
    if not bool(re.search("[a-z]", data)):
        return False
    if not bool(re.search("[0-9]", data)):
        return False
    if not len(data) >= 10:
        return False
    return True


print(checkio('QwErTy911poqqqq'))
