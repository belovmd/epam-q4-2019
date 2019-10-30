"""
Display price of several items
Input:
    - price of one item: dollars, cents
    - count of items
Output:
    price of given count of items: dollars, cents
"""

dollarCount = int(input("Please enter dollars part of price\n"))
centsCount = int(input("Please enter cents part of price\n"))
itemsCount = int(input("Please enter count of items\n"))

price = (dollarCount * 100 + centsCount) * itemsCount
print(
    "Total cost:{dollars} dollars, {cents} cents"
    .format(dollars=price // 100, cents=price % 100))
