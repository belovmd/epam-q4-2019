prices = {'bulba': 0.90, 'tomato': 1.79}
my_purchase = {
    'bulba': 30,
    'tomato': 2}

grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer %.2f roubles' % grocery_bill)
