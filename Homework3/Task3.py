def generate_numbers(n):
    dct = {key: key**2 for key in range(n)[1:]}
    return dct


def count_me_string(str):
    dct = {}

    for symbol in str:
        if symbol in dct:
            dct[symbol] += 1
        else:
            dct[symbol] = 1
    return dct


n = int(input("Enter n: "))
print(generate_numbers(n + 1))

str = input("string")
print(count_me_string(str))
