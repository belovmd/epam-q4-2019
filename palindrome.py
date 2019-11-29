def palindrome(n):
    if n < 0:
        print("NO")
    else:
        k = n
        m = 0
        while k > 0:
            m = 10 * m + k % 10
            k = k // 10

    if (m == n):
        return True
    else:
        return False


palindrome(12321)
palindrome(123)
