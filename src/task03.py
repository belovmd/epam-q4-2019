"""Classic fizz buzz task
Print Fizz if number devided by 3,
Buzz if number devided by 5,
FizzBuzz if number devided by 3 and by 5.
"""

formatlist = ['', 'Fizz', 'Buzz', 'FizzBuzz']

for num in range(1, 101):
    formatlist[0] = num
    print('{}'.format(
        formatlist[(num % 3 == 0) + 2 * (num % 5 == 0)]))
