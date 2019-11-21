""" Create simulator from real life. This can be booking room in hotel,
visit to casino, visit to bar. Create 3-4 objects, that can describe situation.
Objects should contain attributes and methods to simulate some use cases.
Completed program should print object states, it actions (methods) and
objects interaction.
"""

from random import randint


class CreateHuman(object):
    def create_human(self, name, surname):
        self.name = name
        self.surname = surname
        self.salary = randint(1, 15)
        self.money = 0
        self.company = False
        self.company_name = False


class Worker(CreateHuman):

    def __init__(self, name, surname):
        super().create_human(name, surname)

    def raise_salary(self, allowance):
        self.salary += allowance

    def info(self):
        print('My name is {0} {1}. '
              'I want {2} dollar per hour.'
              .format(self.name, self.surname, self.salary))

    def work(self, hours):
        if not self.company:
            money = int(hours * self.salary)
            self.money += money
            print('Salary is {0}. I have {1} dollars now.'
                  .format(money, self.money))
        else:
            print('You work in a company')

    def dismissal(self):
        if self.company:
            self.company.workers.remove(self)
            self.company = False
            self.company_name = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, other_name):
        if other_name.istitle():
            self.__name = other_name
        else:
            print('Name is not title')


class Director(CreateHuman):
    def __init__(self, name, surname, work_experience):
        super().create_human(name, surname)
        self.work_experience = work_experience


class Company(object):
    def __init__(self, company_name, work_cost):
        self.name = company_name
        self.work_cost = work_cost
        self.money = 0
        self.director = False

    def choose_workers(self, *workers):
        self.workers = []
        for worker in workers:
            if worker.salary < self.work_cost and not \
                    worker.company:
                self.workers.append(worker)
                worker.company_name = self.name
                worker.company = self

    def add_director(self, director):
        self.director = director
        if director.work_experience > 3:
            allowance = 100
            director.salary += allowance

    def show_workers(self):
        print('Company {0}'.format(self.name))
        for worker in self.workers:
            worker.info()

    def work(self, hours):
        money = self.work_cost * hours
        for worker in self.workers:
            worker_salary = worker.salary * hours
            worker.money += worker_salary
            money -= worker_salary
        if self.director:
            self.money -= self.director.salary
            self.director.money += self.director.salary
        self.money += money

    def show_director(self):
        if not self.director:
            return "Company {0} doesn't has a director".format(self.name)
        else:
            return 'Director is {0} {1}' \
                .format(self.director.name, self.director.surname)

    def dismiss_worker(self, worker_name, worker_surname):
        for worker in self.worker:
            if worker.name == worker_name and \
                    worker.surname == worker_surname:
                worker.company = False
                worker.company_name = False


def example():
    worker1 = Worker('Ravshan', 'Azu')
    worker2 = Worker('Jamshut', 'Mon')
    worker3 = Worker('Bogdan', 'Tym')
    worker4 = Worker('Sasha', 'Timi')
    director1 = Director('Slava', 'Tom', 2)
    worker2.work(5)
    company1 = Company('Udi', 6)
    worker2.work(5)
    print(company1.show_director())
    company2 = Company('Ralo', 14)
    company1.add_director(director1)
    company1.choose_workers(worker1, worker2, worker3, worker4)
    company2.choose_workers(worker1, worker2, worker3, worker4)
    worker2.work(5)
    company1.show_workers()
    company2.show_workers()
    company1.work(10)
    print(company1.money)
    print(worker2.company_name)
    worker2.dismissal()
    print(worker2.company_name)
    worker2.name = 'jamshut'


if __name__ == '__main__':
    example()
