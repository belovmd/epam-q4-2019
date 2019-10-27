'''
 Purchase money calculation
'''
'''
first way
'''
price1 = 320
price2 = 250
price3 = 855

cost1 = 0
cost2 = 0
cost3 = 0

num1 = int(input("how much quantity of the first item need to buy? \t"))
num2 = int(input("how much quantity of the second item need to buy? \t"))
num3 = int(input("how much quantity of the third item need to buy? \t"))

for i in range(num1):
    cost1 += price1

print("Cost 1 in dollars", cost1 // 100)
print("Cost 1 in cents ", cost1 % 100)

for i in range(num2):
    cost2 += price2

print("Cost 2 in dollars", cost2 // 100)
print("Cost 2 in cents ", cost2 % 100)


for i in range(num3):
    cost3 += price3

print("Cost 3 in dollars", cost3 // 100)
print("Cost 3 in cents ", cost3 % 100)

print("Total cost in dollars:", cost1 // 100 + cost2 // 100 + cost3 // 100)
print("Total cost in cents:", cost1 % 100 + cost2 % 100 + cost3 % 100)


'''
second way
'''
price1_dol = 3
price1_cen = 20

cost4 = 0
cost5 = 0

for i in range(num1):
    cost4 += price1_dol
    cost5 += price1_cen
    if price1_cen >= 100:
        cost4 += 1
        cost5 = 0

print(cost4, cost5)
