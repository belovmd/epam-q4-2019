"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe
situation. Objects should contain attributes and methods to simulate some
use cases. Completed program should print object states, it actions (
methods) and objects interaction."""
# flake8: noqa:H238
import random
import sys


class OrganizedGroup:
    def __init__(self, strength=random.randint(1, 10)):
        self.strength = strength


class CrimeFighter:
    strength = 0

    def eliminate_gang(self, gang):
        self.strength -= 1
        gang.is_eliminated()


class PoliceSquad(OrganizedGroup, CrimeFighter):
    def eliminate_gang(self, gang):
        super().eliminate_gang(gang)
        if not self.strength:
            print("Police squad is destroyed")


class Gang(OrganizedGroup):
    def is_eliminated(self):
        self.strength = 0
        print("Gang was eliminated!")


class OrganizedStructure:
    group_name = ""
    group_type = OrganizedGroup
    group_size = 3
    max_group_number = 5

    def __init__(self):
        setattr(self, self.group_name,
                [self.group_type(self.group_size) for i in
                 range(random.randint(1, self.max_group_number))])

    def count_groups(self):
        return len([group for group in getattr(self, self.group_name) if
                    group.strength > 0])

    def get_groups(self):
        return getattr(self, self.group_name)


class PoliceDepartment(OrganizedStructure):
    group_name = "squads"
    group_type = PoliceSquad
    group_size = 3
    max_group_number = 4

    def find_squad(self):
        return next((squad for squad in getattr(self, self.group_name) if
                     squad.strength > 0), None)


class OCG(OrganizedStructure):
    group_name = "gangs"
    group_type = Gang
    group_size = random.randint(1, 10)
    max_group_number = 15


class Batman(CrimeFighter):
    def __init__(self):
        self.strength = sys.maxsize

    def eliminate_gang(self, gang):
        super().eliminate_gang(gang)
        print("Batman saves Gotham!")


def fight_against_crime():
    ocg = OCG()
    police = PoliceDepartment()
    batman = Batman()
    print("What do we have here: {} squads and {} gangs and Batman".format(
        police.count_groups(), ocg.count_groups()))
    for gang in ocg.get_groups():
        squad = police.find_squad()
        if squad:
            squad.eliminate_gang(gang)
        else:
            batman.eliminate_gang(gang)
        print("Now we have {} squads and {} gangs and Batman".format(
            police.count_groups(), ocg.count_groups()))
    print("All gangs were eliminated!")


fight_against_crime()
