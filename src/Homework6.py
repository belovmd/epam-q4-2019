"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can
describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states,
it actions (methods) and objects interaction.
"""


class Bar(object):
    def __init__(self, name, vodka_price, beer_price, wine_price):
        self.name = name
        self.vodka_price = vodka_price
        self.beer_price = beer_price
        self.wine_price = wine_price

    def menu(self):
        print('Бар', self.name)
        print('Водка', self.vodka_price)
        print('Пиво', self.beer_price)
        print('Вино', self.wine_price)


class ManInBar(object):
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.ethanol = 0
        self.danger_level = 'OK'
        self.card_limit = 1

    def drink(self, type_of_drink, place):
        if self.danger_level == 'DROP DEAD':
            print('No more tonight, wait until tomorrow')
        else:
            if type_of_drink == 'vodka':
                if self.money - place.vodka_price >= 0:
                    self.money -= place.vodka_price
                    self.ethanol += 0.04
                else:
                    print('Not enough funds')
            elif type_of_drink == 'beer':
                if self.money - place.beer_price >= 0:
                    self.money -= place.beer_price
                    self.ethanol += 0.025
                else:
                    print('Not enough funds')
            elif type_of_drink == 'wine':
                if self.money - place.wine_price >= 0:
                    self.money -= place.wine_price
                    self.ethanol += 0.03
                else:
                    print('Not enough funds')
            else:
                print('No such drinks in our place')
        if self.ethanol >= 0.15:
            self.danger_level = 'DROP DEAD'
        elif self.ethanol >= 0.07:
            self.danger_level = 'DRUNK'

    def info(self):
        print('И вот перед нами', self.name)
        print('У него в кармане', self.money)
        print('Уровень этанола в крови', round(self.ethanol, 3))
        print('Состояние -', self.danger_level)

    def borrow(self, friend, ammount):
        if self.danger_level == 'DROP DEAD':
            print('Sorry, you cant take an action, wait until tomorrow')
        else:
            if isinstance(friend, ManInBar):
                if friend.money - ammount > 0:
                    self.money += ammount
                    friend.money -= ammount
                else:
                    print(friend.name, 'said: "Maaan, its too much')

    def cash(self):
        if self.card_limit == 1:
            self.money += 50
            self.card_limit = 0
        else:
            print('Out of money for tonight, wait until tomorrow')

    def tomorrow(self):
        self.ethanol = 0.02
        self.danger_level = 'OK'
        self.card_limit = 1


oyster = Bar('Blue Oyster Bar', 10, 15, 20)
zyba = Bar('Zybitskaya Luxury Place', 20, 25, 40)
oyster.menu()
zyba.menu()
kolya = ManInBar('Николай')
kolya.drink('wine', zyba)
kolya.info()
kolya.drink('wine', zyba)
kolya.info()
kolya.drink('beer', zyba)
kolya.cash()
kolya.info()
kolya.drink('beer', zyba)
kolya.drink('beer', zyba)
maxim = ManInBar('Максим')
maxim.info()
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.info()
# kolya meets maxim in blue oyster bar
kolya.borrow(maxim, 50)
kolya.borrow(maxim, 30)
kolya.info()
maxim.info()
kolya.drink('vodka', oyster)
kolya.drink('vodka', oyster)
kolya.borrow(maxim, 15)
kolya.info()
kolya.tomorrow()
maxim.tomorrow()
kolya.info()
maxim.info()
