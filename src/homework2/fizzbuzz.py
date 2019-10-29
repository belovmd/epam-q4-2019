"""Write a program that prints the numbers from 1 to 100, but
for multiples of three print “Fizz” instead of the number and
for multiples of five print “Buzz”.
For numbers which are multiples of both three and five, print “FizzBuzz”."""
for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0):
        print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0))
    else:
        print(i)
