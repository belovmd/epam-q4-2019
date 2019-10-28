''' Write a program that prints the numbers from 1 to 100, but for
multiples of three print “Fizz” instead of the number and for multiples
of five print “Buzz”. For numbers which are multiples of both three and
five, print “FizzBuzz”. '''

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
