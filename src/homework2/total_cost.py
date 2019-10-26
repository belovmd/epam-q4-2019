dollars = int(input("Enter dollars:"))
cents = int(input("Enter cents:"))
amount = int(input("Enter amount:"))
price = dollars * 100 + cents
total_cost = price * amount
print("Total cost:", total_cost // 100, "dollars", total_cost % 100, "cents")
