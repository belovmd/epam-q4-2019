"""
Create simulator from real life. This can be
booking room in hotel, visit to casino, visit to bar.
Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods
to simulate some use cases.
Completed program should print object states,
it actions (methods) and objects interaction.
Every bar can have it's own menu with unique prices
Each person has his own name, amount of money and
his own norm in drinking alcohol
"""


class Bar(object):
    earned = 0
    name = "Unknown"

    menu_amount = {"beer": 50000,
                   "whiskey": 500,
                   "vodka": 1000}

    menu_prices = {"beer": 5,
                   "whiskey": 10,
                   "vodka": 3}

    menu_portions = {"beer": 500,
                     "vodka": 50,
                     "whiskey": 50}

    # if arg = 0 - set default value
    def __init__(self, name, menu_am, menu_pr):
        if name:
            self.name = name
        if menu_am:
            self.menu_amount = menu_am
        if menu_pr:
            self.menu_prices = menu_pr

    def sell(self, drink):
        self.menu_amount[drink] -= self.menu_portions[drink]
        self.earned += self.menu_prices[drink]


class Person(object):
    name = "Unknown"
    cur_bar = None
    money = 0
    condition = 0
    condition_stages = {"almost_ok": 25,
                        "enough": 50,
                        "stop": 75,
                        "overdose": 100}
    done = False

    # if arg = 0 - set default value
    def __init__(self, name, money, cond_stages, condition):
        if name:
            self.name = name
        if money:
            self.money = money
        if cond_stages:
            self.condition_stages = cond_stages
        if condition:
            self.condition = condition

    def check_condition(self):
        if self.condition >= self.condition_stages["overdose"]:
            self.done = True
            return self.name + " fell asleep"
        if self.condition >= self.condition_stages["stop"]:
            return self.name + " drank too much"
        if self.condition >= self.condition_stages["enough"]:
            return self.name + " is drunk"
        if self.condition >= self.condition_stages["almost_ok"]:
            return "maybe " + self.name + " should buy more"
        else:
            return self.name + " is sober"

    def go_to_bar(self, bar):
        self.cur_bar = bar

    def buy(self, drink):
        if self.done:
            print("{} can't drink - he(she) is sleeping \n"
                  .format(self.name))
            return
        if self.money <= 0:
            print("{} can't drink - he(she) has no money left \n"
                  .format(self.name))

            return
        if drink not in self.cur_bar.menu_amount.keys():
            print("There is no {} in {}"
                  .format(drink, self.cur_bar.name))
            print("{}, you can go to another bar \n".format(self.name))
            return
        if not self.cur_bar.menu_amount[drink]:
            print("There is no {} in {}"
                  .format(drink, self.cur_bar.name))
            print("You can go to another bar \n")
            return

        self.money -= self.cur_bar.menu_prices[drink]
        self.cur_bar.sell(drink)
        self.condition += 20
        self.check_condition()
        print("{} drank one portion of {}".format(self.name, drink))
        print("{} has now {} dollars".format(self.name, self.money))
        print(self.check_condition(), "\n")


superman_stages = {"almost_ok": 10000,
                   "enough": 10000,
                   "stop": 10000,
                   "overdose": 1000}

person1 = Person("Alex", 100, 0, 0)
person2 = Person("Dimon", 20, 0, 0)
superman = Person("Super man", 1000, superman_stages, 0)

bar1 = Bar("Kafedra", 0, 0)
bar2 = Bar("Kvartirnik", {"vodka": 1000}, 0)

person1.go_to_bar(bar1)
person2.go_to_bar(bar1)
superman.go_to_bar(bar1)

for i in range(5):
    person1.buy("whiskey")
    if i < 4:
        person2.buy("beer")
    superman.buy("vodka")

person2.go_to_bar(bar2)
superman.go_to_bar(bar2)

person2.buy("beer")

superman.buy("vodka")

print(person1.name, ":")
print(person1.money, "dollars")
print(person1.check_condition())
print(person2.name, ":")
print(person2.money, "dollars")
print(person2.check_condition())
print(superman.name, ":")
print(superman.money, "dollars")
print(superman.check_condition())
