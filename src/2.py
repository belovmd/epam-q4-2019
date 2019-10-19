import re


print('Hello World')

name = input('What is your name?\n')
print('Hi, %s ' % name)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


def greet(par):
    print('Hello', par)


greet('Jack')
greet('Jill')
greet('Bob')

for test_string in ['555-1212', 'ILLEGAL', 'NiceTryBro']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, ' is valid US local phone number')
    else:
        print(test_string, 'rejected')

prices = {'apple': 0.40, 'banana': 50}
my_purchase = {
    'apple': 1,
    'banana': 6
}
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)
# print(my_purchase[fruit] for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)
