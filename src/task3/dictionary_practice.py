# 3.1 Dict with keys as numbers and values as squares
def generate_numbers(number=20):
    try:
        number = int(number)
    except Exception:
        raise Exception
    return {a: a ** 2 for a in range(number + 1) if a > 0}


# Letter only input raises error:
# generate_numbers('foo')
assert generate_numbers(5.99) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
assert generate_numbers('5') == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
assert generate_numbers(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
assert generate_numbers() == {
    1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
    11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324,
    19: 361, 20: 400}
print(generate_numbers(5))
print(generate_numbers())


# 3.2 Count characters in string
def count_characters(count_me_string):
    try:
        count_me_string = str(count_me_string)
    except Exception:
        raise Exception
    if len(count_me_string) == 0:
        raise ValueError('Empty string input is not allowed')

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890,.;'
    count_me_string = count_me_string.lower()
    return {letter: count_me_string.count(letter)
            for letter in alphabet
            if count_me_string.count(letter) > 0}


# Empty input raises error:
# print(count_characters(''))
assert count_characters(1232.34234) == {'1': 1, '2': 3, '3': 3, '4': 2, '.': 1}
assert count_characters('Neonatal Intensive Care Unit') == {
    'a': 3, 'c': 1, 'e': 4, 'i': 3, 'l': 1, 'n': 5,
    'o': 1, 'r': 1, 's': 1, 't': 3, 'u': 1, 'v': 1
}
print(count_characters('Neonatal Intensive Care Unit # 3'))
