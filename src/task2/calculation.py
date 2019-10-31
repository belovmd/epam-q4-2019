"""Calculate total cost

One item costs M dollars and N cents. Customer bought L items.
Print total price in dollars and cents for L items.
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 60 cents.
"""


dollars, cents = \
    input('Enter one item price in format dollars.cents, like 3.14: ')\
    .split('.')
dollars = int(dollars)
cents = int(cents)
total_cents = dollars * 100 + cents
total_items = int(input("How many items are needed? "))
total_cost = int(total_cents * total_items)
final_dollars = int(total_cost // 100)
final_cents = int(total_cost % 100)
print("Total cost: {} dollars {} cents.".format(final_dollars, final_cents))
