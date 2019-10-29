"""Write a program to calculate total cost.
One item costs M dollars and N cents. Customer bought L items.
Print total price in dollars and cents for L items.
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 60 cents.
"""
dollars = int(input("Enter dollars:"))
cents = int(input("Enter cents:"))
amount = int(input("Enter amount:"))
price = dollars * 100 + cents
total_cost = price * amount
print("Total cost:", total_cost // 100, "dollars", total_cost % 100, "cents")
