"""Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe
situation. Objects should contain attributes and methods to simulate some
use cases. Completed program should print object states, it actions (
methods) and objects interaction."""
# flake8: noqa:H238
import random


class FightUnit:
    """Unit that has strength and can fight with other ones"""

    def __init__(self, strength=random.randint(1, 20), name="Unit"):
        """Init unit with strength and name"""
        self.strength = strength
        self.name = name

    def throw_dice(self):
        """Throw dice to determine luck in fighting"""
        return random.randint(1, self.strength + 1)

    def fight_with_another_unit(self, enemy):
        """Determine luck and destroy unlucky one"""
        self_luck, enemy_luck = self.throw_dice(), enemy.throw_dice()
        if self_luck >= enemy_luck:
            enemy.is_destroyed()
        if self_luck <= enemy_luck:
            self.is_destroyed()

    def is_destroyed(self):
        """Destroy unit"""
        self.strength = 0
        print("{} is destroyed.".format(self.name), end=" ")


class Batman(FightUnit):
    """Batman, fight unit that can lost strength, but every day heals"""
    strength = 40

    def __init__(self):
        """Create Batman with great strength"""
        super().__init__(Batman.strength, "Batman")

    def is_destroyed(self):
        """Batman lost but not defeated"""
        self.strength = 0
        print("{} has lost.".format(self.name), end=" ")

    def is_ready_for_fight(self):
        """Return 1 if strength is positive, else return 0"""
        return int(self.strength > 0)

    def heal_batman(self):
        """Heal Batman to initial strength"""
        self.strength = Batman.strength

    def __rmul__(self, other):
        """define multiplication by a number"""
        if other:
            return self


class OrganizedStructure:
    """Structure that has fight units, can count it, restore from reserve"""
    reserve = 25

    def __init__(self, unit_strength=3, max_units=10, unit_name="Unit"):
        """Create fight units"""
        self.unit_strength = unit_strength
        self.units = [FightUnit(unit_strength, unit_name) for _ in
                      range(random.randint(1, max_units))]

    def count_units(self):
        """Count figth units with nonzero strength"""
        return len(self.get_units())

    def get_units(self):
        """Get figth units with nonzero strength"""
        return [unit for unit in self.units if unit.strength]

    def restore_units(self):
        """Restore units from reserve if it's possible"""
        for unit in self.units:
            if self.reserve and unit.strength < self.unit_strength:
                restore_size = min(self.reserve,
                                   self.unit_strength - unit.strength)
                self.reserve -= restore_size
                unit.strength += restore_size


class PoliceDepartment(OrganizedStructure):
    """Police, can find the strongest unit to send to fight"""

    def find_unit(self):
        """Find and return the strongest unit. Return None if all were
        destroyed"""
        max_strength = max(unit.strength for unit in self.units)
        return None if max_strength == 0 else next(
            unit for unit in self.units if unit.strength == max_strength)


def fight_against_crime():
    days_in_month = 20
    ocg = OrganizedStructure(unit_strength=random.randint(1, 20), max_units=20,
                             unit_name="Criminal group")
    police, batman = PoliceDepartment(unit_name="Police squad"), Batman()
    for day in range(days_in_month):
        print("What we have on {} day: {} squads and {} gangs and {} Batman."
              .format(day + 1, police.count_units(), ocg.count_units(),
                      batman.is_ready_for_fight()))
        for criminal_group in ocg.get_units():
            # while criminal_group.strength:
            fighter = police.find_unit() or batman.is_ready_for_fight() * \
                      batman
            if fighter:
                fighter.fight_with_another_unit(criminal_group)
            else:
                print("Criminal groups won fight this day.")
                break
            print(
                "Now we have {} squads and {} gangs and {} Batman.".format(
                    police.count_units(), ocg.count_units(),
                    batman.is_ready_for_fight()))
        print("By the end of {} day we have: {} squads and {} gangs and {} "
              "Batman."
              .format(day + 1, police.count_units(), ocg.count_units(),
                      batman.is_ready_for_fight()))
        ocg.restore_units(), police.restore_units(), batman.heal_batman()
        if not ocg.count_units():
            print("All criminal groups were destroyed.")
            break
    print("By the end of month we have: {} squads and {} gangs and {} Batman."
          .format(police.count_units(), ocg.count_units(),
                  batman.is_ready_for_fight()))


fight_against_crime()
