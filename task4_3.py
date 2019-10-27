"""
You are given an array of integer arr and a positive integer k.
Print the number of (i, j) pairs where i < j and arr[i] + arr[j] divisible by k

For example,
input:
1 3 2 6 1 2
3

output:
5
"""

arr = [int(i) for i in input().split(' ')]
k = int(input())

result = 0
for index, first in enumerate(arr[:-1]):
    for second in arr[index + 1:]:
        if not (first + second) % k:
            result += 1
print(result)
