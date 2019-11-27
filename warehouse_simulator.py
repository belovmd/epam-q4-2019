"""Create simulator from real life. This can be booking room in hotel, visit
to casino, visit to bar. Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states, it actions (methods) and objects
interaction.
"""


class Warehouse(object):
    """This is simulator of Warehouse.

    Starting parameters:
    money - starting sum of money in dollars
    cheat - difference between purchase price and sale price
    """
    money = 70000
    cheat = 1.1
    materials = {}
    price = {}

    def warehouse_info(self):
        """Prints materials at Warehouse and their quantity."""
        for material in Warehouse.materials.keys():
            print('Quantity of {mater}: {quantity}.'.format(
                mater=material,
                quantity=Warehouse.materials[material]))
        number = 0
        for value in Warehouse.materials.values():
            if value != 0:
                number += 1
        print('Current number of materials in Warehouse is {}.'
              'Current money ballance: {}'.
              format(number, Warehouse.money))

    def material_info(self, material):
        """Shows current info about material."""
        print('Material - {}: Price: {}, Quantity: {}'.format(
            material.material_name,
            Warehouse.price[material.material_name],
            Warehouse.materials[material.material_name]))


class Material(object):
    """Creating materials and adding their quantity and price to Warehouse."""
    price = {}

    def __init__(self, material_name, material_price):
        """Add material to Warehouse."""
        self.material_name = material_name
        self.material_price = material_price
        self.material_quantity = 0
        Warehouse.materials[self.material_name] = self.material_quantity
        Warehouse.price[self.material_name] = self.material_price


class Worker(Warehouse):
    """Creating worker, who can buy/sell materials, extend capacity of

    Warehouse and check about material price raise.
    """

    def material_purchase(self, material, quantity):
        """Material purchase."""
        if quantity * material.material_price <= Warehouse.money:
            Warehouse.materials[material.material_name] += quantity
            Warehouse.money -= quantity * material.material_price
            print('You purchased {}m^3 of {}. Current quantity is {}. '
                  'You spent {}$.'.format(quantity,
                                          material.material_name,
                                          Warehouse.
                                          materials[material.material_name],
                                          quantity *
                                          material.material_price))
        else:
            print('There is not enough money to purchase. Sale some.')

    def material_sale(self, material, quantity):
        """Material sale."""
        if Warehouse.materials[material.material_name] >= quantity:
            Warehouse.materials[material.material_name] -= quantity
            money = quantity * material.material_price * Warehouse.cheat
            Warehouse.money += money
            print('You sale {}m^3 of {}. Current quantity is {}. '
                  'You earn {}$.'.format(quantity,
                                         material.material_name,
                                         Warehouse.
                                         materials[material.material_name],
                                         money))
        else:
            print('There is not enough material to sale. Purchase some.')

    def raise_price(self, material, amount_percent):
        """Checking price raise.

        If price raise more than 5%, we don't buy material.
        """
        if amount_percent > 0.05 * material.material_price:
            print('Price increase too much: {}.'.format(
                material.material_price + amount_percent / 100 *
                material.material_price))
        else:
            material.material_price += \
                amount_percent / 100 * material.material_price
            Warehouse.price[material.material_name] += \
                amount_percent / 100 * material.material_price


class Calculator(Warehouse):
    """Counts the purchase amount of several materials."""

    def calculate(self):
        """Helps to count your purchases and makes "check.txt"."""
        purchases = 'Your purchases:\n'
        summary = 0
        add_to_cart = {}
        for material in Warehouse.materials.keys():
            amount = float(input('Input amount of {}: '.format(
                material)))
            while amount > Warehouse.materials[material]:
                print('Sorry, max is {}'.format(
                    Warehouse.materials[material]))
                amount = float(input('Input amount of {}: '.format(
                    material)))
            add_to_cart[material] = amount
            summary += Warehouse.price[material] * amount
            purchases += '{amnt} m^3 of {mater} will cost {price}$.\n'.format(
                amnt=amount,
                mater=material,
                price=Warehouse.price[material] * amount)
        with open('check.txt', 'w') as check:
            check.write(purchases + '\n' + 'Total cost: ' +
                        str(summary) + '$')
        print('\n' + purchases)
        print('Total cost: ', summary, '$')


if __name__ == '__main__':
    sand = Material('Sand', 15)
    glass = Material('Glass', 20)
    plastic = Material('Plastic', 5)
    stone = Material('Stone', 10)
    metal = Material('Metal', 50)
    water = Material('Water', 20)
    fuel = Material('Fuel', 70)
    warehouse = Warehouse()
    calc = Calculator()
    worker = Worker()
    worker.material_purchase(sand, 1000)
    worker.material_purchase(glass, 300)
    worker.material_purchase(plastic, 300)
    worker.material_purchase(stone, 300)
    worker.material_purchase(fuel, 300)
    warehouse.warehouse_info()
    warehouse.material_info(plastic)
    worker.material_sale(sand, 500)
    worker.material_sale(sand, 200)
    worker.raise_price(fuel, 3)
    warehouse.material_info(fuel)
    worker.material_purchase(fuel, 700)
    calc.calculate()
