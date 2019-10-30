att = 3
while att > 0:
    price = str(input('Input price, separate dollars from cents with "." : '))
    num_of_items = int(input('Input number of items you want to buy: '))
    cents = int(price.split('.')[1])
    if len(str(cents)) <= 2:
        cost = float(price) * num_of_items
        print('Total cost: {0} dollars {1} cents'.format
              (int(str(cost).split('.')[0]),
               int(str(cost).split('.')[1]))
              )
        break
    elif att <= 1:
        print('You entered nonexistenting amount')
        break
    else:
        print('Please input correct amount of cents, you have {0} attempts'.
              format(att-1))
        att -= 1



