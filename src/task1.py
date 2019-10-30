'''Purchase money calculator'''


def money_calculator(dollars, cents, quantity):
    cost = dollars + cents / 100
    dollars = cost * quantity
    cents = int((dollars % 1) * 100)
    return f'Total cost:{int(dollars)} dollars {cents} cents'


if __name__ == '__main__':
    print(money_calculator(3, 20, 3))

