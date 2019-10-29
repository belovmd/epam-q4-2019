"""
Write a program to calculate total cost. One item costs M dollars and N cents.
Customer bought L items. Print total price in dollars and cents for L items.
Input data:  one item price is 3 dollars 20 cents, calculate price for 3 items
Output data: Total cost:  9 dollars 60 cents.

"""

if __name__ == '__main__':
    dollars = int(input('Enter dollars '))
    cents = int(input('Enter cents '))
    quantity = int(input('Enter quantity '))
    total_price = (dollars * 100 + cents) * quantity
    print('Total price: {} dollars '
          '{} cents'.format(total_price // 100, total_price % 100))
