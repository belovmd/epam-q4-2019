"""
Write a program to calculate total cost. One item costs M dollars and N cents.
Customer bought L items.
Print total price in dollars and cents for L items.
For example
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 20 cents.
"""

# There were no additional explanations about input
# so I did it exactly like in example
input_data = input().split(' ')
M, N, L = (int(word) for word in input_data if word.isnumeric())

total_cents = N * L
total_dollars = M * L + total_cents // 100
total_cents %= 100

print("Total cost {} dollars {} cents".format(total_dollars, total_cents))
