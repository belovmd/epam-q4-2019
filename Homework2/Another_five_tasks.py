import math

''' Даны три целых числа. Выведите значение наименьшего из них. '''

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 < number_2 and number_1 < number_3:
    print(number_1)
elif number_2 < number_3:
    print(number_2)
else:
    print(number_3)


''' Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают),
2 (если два совпадает) или 0 (если все числа различны). '''

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
if number_1 == number_2 == number_3:
    print(3)
elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
    print(2)
else:
    print(0)


''' За день машина проезжает n километров. Сколько дней нужно, чтобы проехать
маршрут длиной m километров? Программа получает на вход числа n и m. '''

n = int(input())
m = int(input())
print(math.ceil(m / n))


''' Дано трехзначное число. Найдите сумму его цифр. '''

x = int(input())
sum_of_digits = (x // 100) + (x // 10 % 10) + (x % 10)
print(sum_of_digits)


''' Даны два целых числа A и В. Выведите все числа от A до B включительно, в
порядке возрастания, если A < B, или в порядке убывания в противном случае. '''

A = int(input())
B = int(input())
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)
