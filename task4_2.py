"""
Given N integers, find the minimum and maximum values that can be
calculated by summing exactly M of the N integers. Then print the respective
minimum and maximum values as a single line of two space-separated
long integers.

For example,
input:
5 4
1 3 5 7 9

output:
16 24
"""

N, M = (int(i) for i in input().split(' '))
arr = [int(i) for i in input().split(' ')]

if (M > N) or (len(arr) != N):
    print("Invalid input")
else:
    arr.sort()
    min_sum = sum(arr[:M])
    max_sum = sum(arr[-M:])
    print(min_sum, max_sum)
