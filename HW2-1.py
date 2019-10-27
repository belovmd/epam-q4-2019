"""
Finding palindrome
"""

n = int(input("Enter num: "))

if n < 0:
    print("NO")
else:
    k = n
    m = 0
    while k > 0:
        m = 10 * m + k % 10
        k = k // 10
        print(m)

if (m == n):
    print("YES")
else:
    print("NO")
