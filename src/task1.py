'''Purchase money calculator'''
def money_calculator(cost, quantity):

    return f'Total cost:{int(cost * quantity)} dollars {int((cost*quantity%1)*100)} cents'

if __name__ == '__main__':
    print(money_calculator(3.20, 3))
