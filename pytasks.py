def generate_numbers(input=5):
    import random
    output = []
    i = 0
    while i != input:
        rand_num = random.randint(1, 101)
        output.append(rand_num)
        i += 1
    return output


def count_characters(input=''):
    result = len(input)
    return result


def fizzbuzz():
    i = 0
    while i != 100:
        i += 1
        if i % 15 == 0:
            print('FizzBuzz')
            continue
        elif i % 3 == 0:
            print('Fizz')
            continue
        elif i % 5 == 0:
            print('Buzz')
            continue
        else:
            print(i)


def is_palindrome(input='xxx'):
    revers = str(input[::-1])
    if revers == input:
        return True
    else:
        return False
