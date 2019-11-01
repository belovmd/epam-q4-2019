'''
how many units in the binary
number system of the number n
'''
num = int(input("Enter num: "))
b = ''
counter = 0

while num:
    b = str(num % 2) + b
    num = num // 2

for i in range(len(b)):
    if b[i] == "1":
        counter += 1

print(b)
print(counter)
