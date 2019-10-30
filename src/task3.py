'''FizzBazz'''


def fizz_bazz(range_):
    for digit in range(range_):
        if digit % 15 == 0:
            yield 'FizzBuzz'
        elif digit % 3 == 0:
            yield 'Fizz'
        elif digit % 5 == 0:
            yield 'Buzz'
        else:
            yield digit


if __name__ == '__main__':
    gen = fizz_bazz(100)
    for digit in gen:
        print(digit)
