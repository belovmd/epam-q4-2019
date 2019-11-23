"""Create simulator from real life. This can be booking room in hotel, visit
to casino, visit to bar. Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states, it actions (methods) and objects
interaction.
"""


class Warehouse(object):
    """This is simulator of Warehouse.

    Starting parameters:
    material_limit - material limit in m^3
    money - starting sum of money in dollars
    cheat - difference between purchase price and sale price
    extend_cost - cost in dollars of Warehouse extending at 1m^3
    """
    material_limit = 5000
    money = 70000
    cheat = 1.1
    extend_cost = 10
    materials = {}

    @staticmethod
    def warehouse_info():
        """Prints materials at Warehouse and their Quantity/Capacity."""
        for material in Warehouse.materials.keys():
            print('Quantity/Capacity of {mater}: {amount}/{capacity}.'.format(
                mater=Warehouse.materials[material].material_name,
                amount=Warehouse.materials[material].material_quantity,
                capacity=Warehouse.materials[material].material_limit))
        print('Current number of materials in Warehouse is {}.'.
              format(len(Warehouse.materials)))


class Material(Warehouse):
    """Working with materials at Warehouse."""
    def __init__(self, material_name, material_price):
        """Add material to Warehouse."""
        self.material_name = material_name
        self.material_price = material_price
        self.material_quantity = Warehouse.material_limit
        self.material_limit = Warehouse.material_limit
        Warehouse.materials[self.material_name] = self

    def material_purchase(self, purchase_quantity):
        """Material purchase."""
        if purchase_quantity * self.material_price < Warehouse.money:
            if self.material_quantity + purchase_quantity <= \
                    self.material_limit:
                self.material_quantity += purchase_quantity
                print('You purchased {}m^3 of {}. Current quantity is {}/{}. '
                      'You spent {}$.'.format(purchase_quantity,
                                              self.material_name,
                                              self.material_quantity,
                                              self.material_limit,
                                              purchase_quantity *
                                              self.material_price))
            else:
                print('There will be too much material to store '
                      'at warehouse. Sale some or extend capacity.')
        else:
            print('There is not enough money to purchase. Sale some.')

    def material_sale(self, sale_quantity):
        """Material sale."""
        if self.material_quantity > sale_quantity:
            self.material_quantity -= sale_quantity
            money = sale_quantity * self.material_price * Warehouse.cheat
            Warehouse.money += money
            print('You sale {}m^3 of {}. Current quantity is {}/{}. '
                  'You earn {}$.'.format(sale_quantity,
                                         self.material_name,
                                         self.material_quantity,
                                         self.material_limit,
                                         money))
        else:
            print('There is not enough material to sale. Purchase some.')

    def extend_capacity(self, extend_value):
        if extend_value * Warehouse.extend_cost <= Warehouse.money:
            self.material_limit += extend_value
            Warehouse.money -= extend_value * Warehouse.extend_cost
            print('Capacity extended. Current = {capacity}. '
                  'Spent {money}$.'.format(capacity=self.material_limit,
                                           money=extend_value *
                                           Warehouse.extend_cost))
        else:
            print('Need to sell materials at {sum}$ to extend capacity.'.
                  format(sum=extend_value * Warehouse.extend_cost -
                         Warehouse.money))

    def raise_price(self, amount_percent):
        """Checking price raise.

        If price raise more than 5%, we don't buy material.
        """
        if amount_percent > 0.05 * self.material_price:
            print('Price increase too much: {}.'.format(
                self.material_price + amount_percent / 100 *
                self.material_price))
        else:
            self.material_price += amount_percent / 100 * self.material_price

    def info(self):
        """Shows current info about material."""
        print('Material - {}: Price: {}, In stock: {}/{}'.format(
            self.material_name,
            self.material_price,
            self.material_quantity,
            self.material_limit))


class Calculator(Material):
    """Counts the purchase amount of several materials."""
    @staticmethod
    def calc():
        """Helps to count your purchases and makes "check.txt"."""
        purchases = 'Your purchases:\n'
        summary = 0
        add_to_cart = {}
        for material in Warehouse.materials.keys():
            amount = int(input('Input amount of {}: '.format(
                material)))
            while amount > Warehouse.materials[material].material_quantity:
                print('Sorry, max is {}'.format(
                    Warehouse.materials[material].material_quantity))
                amount = int(input('Input amount of {}: '.format(
                    material)))
            add_to_cart[material] = amount
            summary += Warehouse.materials[material].material_price * amount
            purchases += '{amnt} m^3 of {mater} will cost {price}.\n'.format(
                amnt=amount,
                mater=material,
                price=Warehouse.materials[material].material_price * amount)
        with open('check.txt', 'w') as check:
            check.write(purchases + '\n' + 'Total cost: ' + str(summary))
        print('\n' + purchases)
        print('Total cost: ', summary)


Sand = Material('Sand', 15)
Glass = Material('Glass', 20)
Plastic = Material('Plastic', 5)
Stone = Material('Stone', 10)
Metal = Material('Metal', 50)
Water = Material('Water', 20)
c = Calculator
Fuel = Material('Fuel', 70)
Metal.extend_capacity(1500)
Warehouse.warehouse_info()
Water.material_purchase(800)
Water.extend_capacity(1000)
Water.info()
Water.material_purchase(800)
Water.info()
Water.material_purchase(1750)
Water.material_sale(3000)
Water.material_purchase(1750)
Fuel.info()
Fuel.raise_price(7)
Fuel.raise_price(2)
Fuel.info()
c.calc()
