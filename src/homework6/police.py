"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe
situation. Objects should contain attributes and methods to simulate some
use cases. Completed program should print object states, it actions (
methods) and objects interaction."""
# flake8: noqa:H238
import random
import sys


class FightUnit:
    def __init__(self, strength=random.randint(1, 20)):
        self.strength = strength

    def throw_dice(self):
        return random.randint(1, self.strength + 1)


class CrimeFighter(FightUnit):
    strength = 0

    def fight_gang(self, gang):
        self_luck, gang_luck = self.throw_dice(), gang.throw_dice()
        if (self_luck > gang_luck):
            self.strength -= 1
            gang.is_eliminated()
        elif (self_luck == gang_luck):
            self.strength = 0
            gang.is_eliminated()
        else:
            self.strength = 0


class PoliceSquad(CrimeFighter):
    def fight_gang(self, gang):
        super().fight_gang(gang)
        if not self.strength:
            print("Police squad is destroyed")


class Gang(FightUnit):
    def is_eliminated(self):
        self.strength = 0
        print("Gang was eliminated!")


class OrganizedStructure:
    group_name = ""
    group_type = FightUnit
    group_size = 3
    max_group_number = 10
    reserve = 30

    def __init__(self):
        setattr(self, self.group_name,
                [self.group_type(self.group_size) for i in
                 range(random.randint(1, self.max_group_number))])

    def count_groups(self):
        return len([group for group in getattr(self, self.group_name) if
                    group.strength > 0])

    def get_groups(self):
        return getattr(self, self.group_name)

    def restore_groups(self):
        for group in self.get_groups():
            if self.reserve and group.strength < self.group_size:
                restore_size = min(self.reserve,
                                   self.group_size - group.strength)
                self.reserve -= restore_size
                group.strength += restore_size


class PoliceDepartment(OrganizedStructure):
    group_name = "squads"
    group_type = PoliceSquad
    group_size = 3
    max_group_number = 10

    def find_squad(self):
        max_strength = max(
            squad.strength for squad in getattr(self, self.group_name))
        return None if max_strength == 0 else next(
            (squad for squad in getattr(self, self.group_name) if
             squad.strength == max_strength), None)


class OCG(OrganizedStructure):
    group_name = "gangs"
    group_type = Gang
    group_size = random.randint(1, 10)
    max_group_number = 20


class Batman(CrimeFighter):
    def __init__(self):
        super().__init__(sys.maxsize)

    def fight_gang(self, gang):
        super().fight_gang(gang)
        if not self.strength:
            print("Batman can't destroy gang. Should try another time.")
            self.__init__()
        else:
            print("Batman saves Gotham!")


def fight_against_crime():
    days_in_month = 31
    ocg, police, batman = OCG(), PoliceDepartment(), Batman()
    for day in range(days_in_month):
        print("What we have on {} day: {} squads and {} gangs and Batman"
              .format(day + 1, police.count_groups(), ocg.count_groups()))
        for gang in ocg.get_groups():
            while gang.strength:
                squad = police.find_squad()
                if squad:
                    squad.fight_gang(gang)
                else:
                    batman.fight_gang(gang)
            print("Now we have {} squads and {} gangs and Batman"
                  .format(police.count_groups(), ocg.count_groups()))
        print("By the end of {} day we have: {} squads and {} gangs and Batman"
              .format(day + 1, police.count_groups(), ocg.count_groups()))
        ocg.restore_groups(), police.restore_groups()
    print("By the end of month we have: {} squads and {} gangs and Batman"
          .format(police.count_groups(), ocg.count_groups()))


fight_against_crime()
