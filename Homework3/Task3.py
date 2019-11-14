"""Task 3 from Homework3 (dictionaries)"""


def generate_numbers(n=20):
    return {key: key**2 for key in range(1, n + 1)}


def count_me_string(str1):
    """Returns the numbers of each character in a count_me_string argument"""
    dct = {elem: str1.count(elem) for elem in str1}
    return dct


n = int(input("Enter n: "))
print(generate_numbers(n))

str1 = input("string: ")
print(count_me_string(str1))
