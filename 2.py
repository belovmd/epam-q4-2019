'''
 Purchase money calculation
'''

M = 3
N = 20
L = int(input("How much:"))
cost1 = 0
cost2 = 0

for i in range(L):
    cost1 += M
    cost2 += N
    if cost2 >= 100:
        cost1 += 1
        cost2 = 0

print(cost1, cost2)
