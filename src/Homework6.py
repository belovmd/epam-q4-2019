"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can
describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states,
it actions (methods) and objects interaction.
"""


class Bar(object):

    """Бары: ассортимент и цены"""
    def __init__(self, name, vodka_price, beer_price, wine_price):
        """Создание бара"""
        self.name = name
        self.vodka_price = vodka_price
        self.beer_price = beer_price
        self.wine_price = wine_price

    def menu(self):
        """Информация о баре"""
        print('Бар', self.name)
        print('Водка', self.vodka_price)
        print('Пиво', self.beer_price)
        print('Вино', self.wine_price)


class ManInBar(object):

    """Люди"""
    ETHANOL = 0
    DANGER_LEVEL = 'В ПОРЯДКЕ'

    def __init__(self, name, money, card_limit):
        """Создаем человека, задаем имя, деньги и лимит по карте"""
        self.name = name
        self.money = money
        self.card_limit = card_limit

    def drink(self, type_of_drink, place):
        """Симулируем покупку и употребление человеком алкоголя"""
        if self.DANGER_LEVEL == 'БЕЗ ЧУВСТВ':
            print('Хватит на сегодня, подожди завтра')
            return

        if type_of_drink == 'vodka':
            if self.money - place.vodka_price >= 0:
                self.money -= place.vodka_price
                self.ETHANOL += 0.04
            else:
                print('Недостаточно средств')
                return
        elif type_of_drink == 'beer':
            if self.money - place.beer_price >= 0:
                self.money -= place.beer_price
                self.ETHANOL += 0.025
            else:
                print('Недостаточно средств')
                return
        elif type_of_drink == 'wine':
            if self.money - place.wine_price >= 0:
                self.money -= place.wine_price
                self.ETHANOL += 0.03
            else:
                print('Недостаточно средств')
                return
        else:
            print('Такого у нас не наливают')

        if self.ETHANOL >= 0.15:
            self.DANGER_LEVEL = 'БЕЗ ЧУВСТВ'
        elif self.ETHANOL >= 0.07:
            self.DANGER_LEVEL = 'ПЬЯН'

    def info(self):
        """Информация о текущем состоянии человека"""
        print('И вот перед нами', self.name)
        print('У него в кармане', self.money)
        print('Уровень этанола в крови', round(self.ETHANOL, 3))
        print('Состояние -', self.DANGER_LEVEL)

    def borrow(self, friend, ammount):
        """Симулируем заём денег у друга, можно взять не больше половины"""
        if self.DANGER_LEVEL == 'БЕЗ ЧУВСТВ':
            print('Не в состоянии двинуться')
        else:
            if isinstance(friend, ManInBar):
                if friend.money - ammount >= friend.money / 2:
                    self.money += ammount
                    friend.money -= ammount
                else:
                    print(friend.name, 'отвечает: "Чувак, у меня столько нет"')

    def cash(self, ammount):
        """Симулируем снятие денег с карты"""
        if self.card_limit - ammount >= 0:
            self.money += ammount
            self.card_limit -= ammount
        else:
            print('На вашей карте закончились средства')

    def tomorrow(self):
        """Наступление дивного нового завтра для человека"""
        self.ETHANOL = 0.02
        self.DANGER_LEVEL = 'В ПОРЯДКЕ'


oyster = Bar('Blue Oyster Bar', 10, 15, 20)
zyba = Bar('Zybitskaya Luxury Place', 20, 25, 40)
oyster.menu()
zyba.menu()
kolya = ManInBar('Николай', 100, 50)
kolya.drink('wine', zyba)
kolya.info()
kolya.drink('wine', zyba)
kolya.info()
kolya.drink('beer', zyba)
kolya.cash(30)
kolya.info()
kolya.drink('beer', zyba)
kolya.drink('beer', zyba)
maxim = ManInBar('Максим', 200, 100)
maxim.info()
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.drink('beer', oyster)
maxim.info()
# kolya meets maxim in blue oyster bar
kolya.borrow(maxim, 150)
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
