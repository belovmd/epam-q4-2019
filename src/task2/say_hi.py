"""Introduce a person with the given parameter's attributes."""


def say_hi(name: str, age: int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
