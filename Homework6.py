import matplotlib.pyplot as plt
import random
plt.style.use('ggplot')

''' Our aim was to create an improved model
    of bacterial cells growth and death in vitro,
    taking into consideration inappropriate environment
    The original model may be checked at the 14 page of
    "BRS Microbiology and Immunology, 6th edition"
    This script contains:
    class Bacteria - to describe bacterial cells
    class Medium - to describe environment and the experiment
    class Scientist - to describe and visualize the results
    and to describe the scientist
    function go_on - to start and run the experiment properly'''


class Bacteria(object):

    exp_data = list()
    bacteria_count = list()

    def __init__(self, species, risk, bacteria_count):
        """species - variable to describe the name of bacteria

        risk - variable to describe risk of bacterial
        death out of inappropriate media

        bacteria_count - contains a list, where each bacteria
        is an integer [1], so we'll be able to manipulate
        with each bacteria in future

        """

        self.species = species
        self.risk = risk
        self.bacteria_count = list(1 for x in range(bacteria_count))

    def bacterias_dividing(self):
        self.bacteria_count = self.bacteria_count * 2
        print('Bacterias are growing! Now there are ',
              len(self.bacteria_count), ' of them!')
        self.exp_data.append(len(self.bacteria_count))

    def bacterias_remaining(self):
        self.exp_data.append(len(self.bacteria_count))

    def description(self):
        print('Hi! I am ', self.species)

    def kill_bacteria(self):
        if len(self.bacteria_count) > 0:
            del(self.bacteria_count[len(self.bacteria_count) - 1])

    def internal_death(self):
        i = 0
        ln = len(self.bacteria_count)
        while i != ln:
            rnd = random.random()
            if rnd > self.risk:
                i += 1
            else:
                i += 1
                self.kill_bacteria()


class Medium(object):
    continuation = True

    def __init__(self, agar, bacterial_life_cycles_limit,
                 bacterial_remaining_cycles_limit, survival_rate):
        """agar - variable to describe the medium (environment)

        bacterial_life_cycles_limit - contains an integer to describe
        how many divisions bacterias will be able to provide

        bacterial_remaining_cycles_limit - contains an integer to describe
        how many life cycles they'll have
        after they won't be able to divide anymore

        survival_rate - describes which % of bacterias will survive 1 life
        cycle without food

        """

        self.agar = agar
        self.bacterial_life_cycles_limit = bacterial_life_cycles_limit
        self.bacterial_remaining_cycles_limit =\
            bacterial_remaining_cycles_limit
        self.survival_rate = survival_rate

    def experiment_stage1(self, bct_count):
        bct_count = len(bct_count)
        if self.bacterial_life_cycles_limit >= bct_count > 0:
            self.bacterial_life_cycles_limit = \
                self.bacterial_life_cycles_limit - bct_count
            print('exp is going on!', self.bacterial_life_cycles_limit)
        else:
            self.continuation = False
            print('The End of the 1st stage!')

    def experiment_stage2(self, bct_count):
        """length_stage2 is multiplied for better visualization"""
        bct_count = len(bct_count)
        if bct_count != 0:
            length_stage2 = round(self.bacterial_remaining_cycles_limit /
                                  bct_count) * 10
            i = 0
            while i != length_stage2:
                Bacteria.exp_data.append(bct_count)
                i += 1

    def experiment_stage3(self, bct_count):
        bct_count = len(bct_count)
        if bct_count != 0:
            while bct_count >= 0:
                bct_count = round(bct_count * self.survival_rate)
                print(bct_count, 'bacterias are still alive')
                if bct_count > 0:
                    Bacteria.exp_data.append(bct_count)
                    if Bacteria.exp_data[len(Bacteria.exp_data) - 1] == \
                       Bacteria.exp_data[len(Bacteria.exp_data) - 2]:
                        break
                elif bct_count == 0:
                    Bacteria.exp_data.append(bct_count)
                    break


class Scientist(object):
    def __init__(self, name):
        self.name = name

    def my_name(self):
        print('Hi! My name is ', self.name)

    def results(self):
        plt.plot(Bacteria.exp_data)
        plt.savefig('result_exp.png')
        plt.show()


def go_on():
    bact = Bacteria('Pseudomonas aerugenosa', 0.4, 5)
    bact.description()
    med = Medium('MacConkey Agar', 1000000, 1000000, 0.85)
    sci = Scientist('Maxim Belov')
    while med.continuation:
        bact.internal_death()
        bact.bacterias_dividing()
        med.experiment_stage1(bact.bacteria_count)
    med.experiment_stage2(bact.bacteria_count)
    med.experiment_stage3(bact.bacteria_count)
    sci.results()


if __name__ == '__main__':
    go_on()
