""" Purchase money calculation
Write a program to calculate total cost. One item costs M dollars and N cents. Customer bought L items. Print total
price in dollars and cents for L items. For example Input data:  one item price is 3 dollars 20 cents,
calculate price for 3 items Output data: Total cost:  9 dollars 20 cents.
"""

dollars = int(input("Enter price (dollars)\n"))
cents = int(input("Enter price (cents)\n"))
items_number = int(input("Enter number of items\n"))

item_price = dollars + cents / 100
total_price = items_number * item_price
total_dollars = round(total_price // 1)
total_cents = round((total_price % 1) * 100)
print("Total cost: {0} dollars {1} cents".format(total_dollars, total_cents))
