"""Introduce a person with the given parameter's attributes."""


def say_hi(name: str, age: int) -> str:
    return "Hi. My name is {} and I'm {} years old".format('Alex', 32)


print(say_hi("Alex", 32))
