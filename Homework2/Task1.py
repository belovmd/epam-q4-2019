"""
1-st task from Homework1
"""

str1 = input("Enter your string: ")
sim = len(str1) // 2 + len(str1) % 2
i = 0

while i < sim:
    if (str1[i] != str1[len(str1) - i - 1]) and \
            (str1[i].swapcase() != str1[len(str1) - i - 1]):
        print("It is not a palindrome")
        break
    i += 1
else:
    print("It is a palindrome")
