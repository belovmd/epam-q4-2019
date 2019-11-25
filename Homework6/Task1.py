""" Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe
situation. Objects should contain attributes and methods to simulate
some use cases. Completed program should print object states, it actions
(methods) and objects interaction.
    There is aggregation in created classes. Person can visit any bar
spending his money and can take debt. """


class Bar(object):
    def __init__(self, name):
        self.name = name
        self.visitors = {}

    def visited(self, person):
        """Counts how many times a person visited this bar """
        self.visitors[person] = self.visitors.get(person, 0) + 1
        print('{}: {} visited us!'.format(self.name, person.name))

    def show_person_visits(self, person):
        """Shows how many times a person visited this bar """
        visits = self.visitors.get(person, 0)
        str_to_format = '{}: {} visited us {} time(s)'
        print(str_to_format.format(self.name, person.name, visits))


class Person(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.debt = 0

    def go_to_bar(self, bar, spent_money):
        """Person chooses bar to visit and set money he wants to spend.

        If he has not enough money, he borrows it.
        After that choosen bar's method "visited" is called
        """
        if spent_money <= self.money:
            self.money -= spent_money
        else:
            borrowed_money = spent_money - self.money
            self.debt += borrowed_money
            self.money = 0
            print('{}: I borrowed {}$'.format(self.name, borrowed_money))
        print('{}: I spent {}$'.format(self.name, spent_money))
        return bar.visited(self)

    def show_balance(self):
        """Shows person's balance """
        print('{}: I have {}$'.format(self.name, self.money))


class Deputy(Person):
    def __init__(self, name, money):
        """Deputy is always richer twice """
        super().__init__(name, money)
        self.money = money * 2


class Teacher(Person):
    @property
    def debt(self):
        return self._debt

    @debt.setter
    def debt(self, value):
        """Teacher's debt can't be more than 1000$ """
        if value > 1000:
            raise ValueError('{}, your debt is too high'.format(self.name))
        self._debt = value


bar_1 = Bar('Best')
bar_2 = Bar('Hot')
andrey = Deputy('Andrey', 1000)
ivan = Teacher('Ivan', 100)
andrey.go_to_bar(bar_1, 300)
ivan.go_to_bar(bar_2, 100)
ivan.go_to_bar(bar_2, 500)
ivan.show_balance()
andrey.show_balance()
bar_1.show_person_visits(andrey)
bar_1.show_person_visits(ivan)
bar_2.show_person_visits(ivan)
