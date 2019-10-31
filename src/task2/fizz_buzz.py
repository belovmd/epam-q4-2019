"""FizzBuzz

A program that prints the numbers from 1 to 100,
for multiples of three print “Fizz” instead of the number,
for multiples of five print “Buzz”,
for numbers which are multiples of both three and five, print “FizzBuzz”.
"""


for number in range(1, 100):
    if number % 3 == 0:
        print("Fizz")
        if number % 5 == 0:
            print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
