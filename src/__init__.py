parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


def greet(name):
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

prices = {'apple': 3.40, 'banana': 6.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

name1 = input('What is your name?\n')
print('Hi, %s.' % name1)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print('iteration {iteration} is {name}'.format(iteration=i, name=name))

a, b = 3, 4
print(a, b)
