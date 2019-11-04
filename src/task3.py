"""Dictionary practice"""


# 1
def generate_numbers(num=20):
    dct = dict()

    for el in range(num + 1):
        dct[el] = el**2

    return dct


print(generate_numbers(3))
print(generate_numbers())


# 2
def count_characters(count_me_string):
    dct = dict()

    for char in count_me_string:
        if char in dct.keys():
            dct[char] += 1
        else:
            dct[char] = 1

    return dct


print(count_characters("abcdefgabc"))
