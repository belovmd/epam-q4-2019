"""
Task from Checkio.
Check if string length >= 10 and it has at least one uppercase letter, one lowercase letter and one digit
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

assert checkio('A1213pokl') == False, "1st example"
assert checkio('bAse730onE4') == True, "2nd example"
assert checkio('asasasasasasasaas') == False, "3rd example"
assert checkio('QWERTYqwerty') == False, "4th example"
assert checkio('123456123456') == False, "5th example"
assert checkio('QwErTy911poqqqq') == True, "6th example"
