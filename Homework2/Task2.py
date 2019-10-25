"""
2-nd task from Homework2
"""

print("One item price is M dollars N cents. Customer bought L items.")
M = int(input("Enter M : "))
N = int(input("Enter N : "))
L = int(input("Enter L : "))

dollars = M * L + N * L // 100
cents = N * L % 100

print("Total cost: {dollars} dollars {cents} cents".format(dollars=dollars, cents=cents))
