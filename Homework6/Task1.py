""" Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe
situation. Objects should contain attributes and methods to simulate
some use cases. Completed program should print object states, it actions
(methods) and objects interaction.
    There is aggregation in created classes. Person can visit any bar
spending his money, some objects can take debt, all classes communicate
with each other and can count own money. """


class Bar(object):
    def __init__(self, name):
        self.name = name
        self.income = 0

    def visited(self, visitor_money):
        if visitor_money:
            print('{}: Thank you!'.format(self.name))
        else:
            print('{}: Give us anything!'.format(self.name))
        self.income += visitor_money

    def total_income(self):
        print('{}: Today we earned {}$'.format(self.name, self.income))


class Person(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def go_to_bar(self, bar_name, spent_money):
        if spent_money <= self.money:
            self.money -= spent_money
        else:
            spent_money = self.money
            self.money = 0
        print('{}: I spent {}$'.format(self.name, spent_money))
        return bar_name.visited(spent_money)

    def show_balance(self):
        print('{}: I have {}$'.format(self.name, self.money))


class Deputy(Person):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.money = money * 2


class Teacher(Person):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.debt = 0

    def take_debt(self, amount):
        if amount <= 500:
            self.money += amount
            self.debt += amount
            print('{}: I took in debt {}$'.format(self.name, amount))
        else:
            print(self.name + ', please, go home!')

    def show_balance(self):
        real_amount = self.money - self.debt
        if real_amount:
            print('{}: My real balance is {}$'.format(self.name, real_amount))
        else:
            print('{}: My real debt is {}$'.format(self.name, -real_amount))


bar_1 = Bar('Best')
bar_2 = Bar('Hot')
andrey = Deputy('Andrey', 1000)
ivan = Teacher('Ivan', 100)
andrey.go_to_bar(bar_1, 300)
andrey.go_to_bar(bar_2, 500)
andrey.show_balance()
ivan.go_to_bar(bar_1, 100)
ivan.go_to_bar(bar_2, 0)
ivan.take_debt(400)
ivan.go_to_bar(bar_2, 100)
ivan.show_balance()
bar_1.total_income()
bar_2.total_income()
