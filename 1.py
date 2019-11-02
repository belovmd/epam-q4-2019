"""
Finding palindrome
"""
h = int(input("Enter num: "))

k = abs(h)
m = 0
while k > 0:
    m = 10 * m + k % 10
    k = k // 10

if (m == abs(h)):
    print("YES")
else:
    print("NO")
