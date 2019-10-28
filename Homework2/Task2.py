''' Write a program to calculate total cost. One item costs M dollars and N
cents. Customer bought L items. Print total price in dollars and cents for
L items.
For example
Input data: one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 60 cents. '''

dollars, cents, items = (int(i) for i in input('Price and items: ').split())
cents_in_dollars = dollars * 100
total_cents = (cents_in_dollars + cents) * items
cost_dollars, cost_cents = total_cents // 100, total_cents % 100
print('Total cost: {} dollars {} cents'.format(cost_dollars, cost_cents))
