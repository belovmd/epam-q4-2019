# Multiply: multiply 2 numbers
# Easy Unpack: return 1st, 3rd and second to last element from tuple
# Index Power:power Nth element of list in the N degree,
# if x[N] doesn't exists then return (-1)
# Digits Manipulation:Multiply all but 0 digits of positive integers.
# Secret Message:Gather all capital letters in one word
# in the order that they appear in the chunk of text.


# PALINDROME
print('input number')
n = int(input())
ONum = n
ost = 0
RNum = 0
while n != 0:
    ost = n % 10
    RNum = RNum * 10 + ost
    n = n // 10
if ONum == RNum:
    print(ONum, 'is a palindrome')
else:
    print(ONum, 'is not a palindrome')

# MULTIPLIER
print('input one item price is')
price = float(input())
print('input count')
cnt = float(input())
summa = 0
summa = (price * cnt)
print('your total=', int(summa), 'dollars',
      round((summa - int(summa)) * 100), 'cents')

# FIZZBUZZ
num = 1
while num <= 100:
    if (num % 3) == 0:
        if (num % 5) == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif (num % 5) == 0:
        print('Buzz')
    else:
        print(num)
    num += 1
