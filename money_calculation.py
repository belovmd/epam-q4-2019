price = str(input('Input price, separate dollars from cents with "." : '))
num_of_items = int(input('Input number of items you want to buy: '))
dollars = int(price.split('.')[0])
cents = int(price.split('.')[1])
print('One item price is {0} dollars {1} cents'.format(dollars, cents))
if cents * num_of_items >= 100:
    print('Total cost: {0} dollars {1} cents'.format
          (dollars * num_of_items + (cents * num_of_items) // 100,
           (cents * num_of_items) % 100))
else:
    print('Total cost: {0} dollars {1} cents'.format
          (dollars * num_of_items, cents * num_of_items))
