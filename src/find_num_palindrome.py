"""Non-recursive finding number palindrome."""


NUMBER = int(input("Enter number: "))
temp_number = NUMBER
reverse_number = 0

for i in (0, temp_number // 2):
    if temp_number == 0:
        break
    reverse_number = (reverse_number * 10) + (temp_number % 10)
    temp_number //= 10

if reverse_number == NUMBER:
    print("yes")
else:
    print("no")
