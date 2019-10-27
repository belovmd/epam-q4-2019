"""
Write a program that prints the numbers from 1 to 100,
but for multiples of three print “Fizz” instead of the number
and for multiples of five print “Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”.
"""

for num in range(1, 101):
    if not num % 3:
        if not num % 5:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif not num % 5:
        print("Buzz")
    else:
        print(num)
