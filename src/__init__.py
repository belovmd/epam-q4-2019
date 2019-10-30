# https://py.checkio.org/ (all tasks)
# 1.Multiply: multiply 2 numbers
# 2.Easy Unpack: return 1st, 3rd and second to last element from tuple
# 3.Index Power:Enter N. Raise Nth element of the array to the Nth power,
# if x[N] doesn't exists then return (-1)
# 4.Digits Manipulation:Multiply all but 0 digits of positive integers.
# 5.Secret Message:Gather all capital letters in one word
# in the order that they appear in the chunk of text.


# PALINDROME
print('input number')
n = int(input())
o_num = n
ost = 0
r_num = 0
while n != 0:
    ost = n % 10
    r_num = r_num * 10 + ost
    n = n // 10
if o_num == r_num:
    print(o_num, 'is a palindrome')
else:
    print(o_num, 'is not a palindrome')

# MULTIPLIER
print('input one item price in dollars:')
price_d = int(input())
print('input one item price in cents:')
price_c = int(input())
print('input count')
cnt = int(input())
summa = 0
if len(str(price_c)) > 2:
    print('incorrect cents ammount')
else:
    summa = (price_d + price_c / 100) * cnt
    print('your total=', int(summa), 'dollars',
          round((summa - int(summa)) * 100), 'cents')

# FIZZBUZZ
num = 1
while num <= 100:
    if (num % 15) == 0:
        print('FizzBuzz')
    elif (num % 3) == 0:
        print('Fizz')
    elif (num % 5) == 0:
        print('Buzz')
    else:
        print(num)
    num += 1
