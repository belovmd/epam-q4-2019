class Person(object):
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        print("Information about the person:", name, age, money)


class Dealer(Person):
    def start_game(self):
        print("The game began")


class Gamer(Person):
    def play_casino(self, how_money):
        self.money -= how_money
        print("amount of money to play:", how_money, "Money:", self.money)

    def win(self):
        self.money += self.money
        print(self.name, "Won!! Money:", self.money)

    def defeat(self):
        print(self.name, "Lost money(")


if __name__ == "__main__":
    dealer = Dealer("Nick", 43, 0)
    first_person = Gamer("John", 33, 200)
    second_person = Gamer("Ann", 28, 450)
    dealer.start_game()
    first_person.play_casino(33)
    first_person.win()
    second_person = Gamer("Ann", 28, 450)
    second_person.play_casino(100)
    second_person.defeat()
