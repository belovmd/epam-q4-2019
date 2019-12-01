from abc import ABC
from abc import abstractmethod
import random

"""Homework 6 - Kitchen

This program describe family using refrigerators. Users (parents and children)
can put and take products from refrigerators, eat product. Children can also
hit refrigerator, and if it will broke, parents need call to the master.
"""


class User(object):
    """User is person who can use refrigerator"""

    def __init__(self, name):
        self.name = name

    def take_product(self, product):
        """Method try to take product

        Method automatically understand, in which refrigerator product is.
        If refrigerator is broken or product not in it, we do nothing.
        Otherwise user take product, and cells where it lie become free.
        """

        refr = product.location
        if not refr:
            print('{product_} is in kitchen, not in'
                  ' refrigerator'.format(product_=product.name))
        elif refr.broken:
            print('{refr_} is broken!'.format(refr_=refr))
        else:
            print('{user_} take {prod} from {refr_}'.format(user_=self.name,
                                                            prod=product.name,
                                                            refr_=refr.name,
                                                            ))
            refr.occupied_cells[product.pr_type] -= product.size
            product.location = None

    def put_product(self, refr, product):
        """Method try to put product in refrigerator

        In cases:
            1) refrigerator is broken
            2) product is already in refrigerator
            3) it it's not enough place in appropriate camera
        we will not put product in refrigerator.
        """
        if refr.broken:
            print('{refr_} is broken!'.format(refr_=refr.name))
        elif product.location == refr:
            print('{prod} is already in {refr_}!'.format(prod=product.name,
                                                         refr_=refr.name))
        else:
            camera_type = product.pr_type
            if refr.occupied_cells[camera_type] + product.size <= \
                    refr.capacity[camera_type]:
                product.location = refr
            else:
                print('{user_name} can\'t put {product_} in {refr_} - not '
                      'enough place!'.format(user_name=self.name,
                                             product_=product.name,
                                             refr_=refr.name))

    def eat(self, product):
        """User will try to eat product

        User can eat product only if it is not in refrigerator, and product
        object will be deleted forever
        """
        if not product.location:
            print('{user_} cant eat product from refrigerator!'.format(
                user_=self.name))
        else:
            print('{user_} eat {product_}'.format(user_=self.name,
                                                  product_=product.name))
            del product


class Parent(User):
    """Parent is User who can call to master, pay and earn money"""
    money = 1400

    def call_to_master(self, master, refr):
        """Using this method parent can call to master.

       After call master will try to fix refrigerator using master.try_to_fix
        method. This method returns result (True o False), and this result will
        be printed
        """
        job_result = master.try_to_fix(self, refr)
        print('{user_} called to {master_}.'.format(user_=self.name,
                                                    master_=master.name),
              end=' ')
        print('He fixed it' if job_result else 'He can\'t fix it')

    def earn_money(self, salary=200):
        """Parent get some money after this method"""
        self.money += salary


class Child(User):
    """Child is user who can hit refrigerator"""

    def hit_fridge(self, refr):
        """After hit refriger. will be broken with a thirty percent chance """
        if random.random() < 0.3:
            refr.broken = True
            print('{child_name} broke {refr_}!'.format(child_name=self.name,
                                                       refr_=refr.name))
        else:
            print('{child_name} hit {refr_}, but not broke.'.format(
                child_name=self.name,
                refr_=refr.name))


class Master(object):
    """Master is a person who can fix refrigerators if he have enough skill

    P.S. I understand that coeefs, fix_difficulty and skills_profit can be
    properties of Refrigerator class and it better for OOP conception. But
    it will make my program more difficult for understanding. So, that's why
    I create this dicts in Master class.
    """
    money = 100
    max_skill = 20
    study_cost = 100
    coeefs = {'The Netherlands': 1.5, 'Belarus': 1}
    fix_difficulty = {'The Netherlands': 1.5, 'Belarus': 1}
    skills_profit = {'The Netherlands': 0.2, 'Belarus': 0.5}

    def __init__(self, skill, name='Master', company='own'):
        self.skill = skill
        self.name = name
        self.company = company

    def advertisement(self):
        """Advertising of master. Skills always increase by two"""
        print('Highly skilled master {master_name} from {company_name} company'
              ' is looking for work! My skill is {master_skill}. Prices:\n'
              'Import refrigerator: {price_import_refr}\nDomestic '
              'refrigerator: {price_domestic_refr}'.
              format(master_name=self.name,
                     company_name=self.company,
                     master_skill=str(self.skill + 2),
                     price_import_refr=str(
                         self.skill * 100 * self.coeefs['The Netherlands']),
                     price_domestic_refr=str(
                         self.skill * 100 * self.coeefs['Belarus'])
                     ))

    def try_to_fix(self, customer, refr):
        """Master will try to fix refrigerator

        Price formula: skill * 100 * сoeff
        Master can fix refrigerator only if he has enough skill.
        If not - consultation is free.
        After fixing master improve skills and earn money.
        Payment is made by the client (Parent)
        """

        if self.skill >= self.fix_difficulty[refr.made_in]:
            refr.broken = False
            customer.money -= self.skill * 100 * self.coeefs[refr.made_in]
            self.skill += self.skills_profit[refr.made_in]
            return True
        return False

    def study(self):
        """Master can pay money and improve his skills"""
        if self.money >= self.study_cost:
            self.money -= self.study_cost
            self.skill += 1
        else:
            print('{master_name} don\'t have enough money to study'.format(
                master_name=self.name))


class Product(object):
    """Product is some food we can eat or put to refrigerator

    It can be cold and freeze type.
    Every product aso have size - it shows how many cells this product need
    """
    location = None

    def __init__(self, name, pr_type='cold', size=1):
        self.name = name
        self.pr_type = pr_type
        self.size = size


class Refrigerator(ABC):
    """Refrigerator is place where we can save products

    New refrigerator always is empty and able to work
    """
    occupied_cells = {'freeze': 0, 'cold': 0}
    broken = False

    @property
    @abstractmethod
    def models_capacity(self):
        return self.models_capacity

    def __init__(self, name, model):
        self.name = name
        self.capacity = self.models_capacity[model]

    @classmethod
    def create_or_update_model(cls, model, freeze_cam_capacity,
                               cold_cam_capacity):
        """Change models characteristics, or create if it is new model"""
        cls.models_capacity[model] = {'freeze': freeze_cam_capacity,
                                      'cold': cold_cam_capacity}

    def display_info(self):
        """Show information about refrigerator and free cells"""
        print(
            'It is {refr_type} aka {refr_name}\nNow it is {free_cold_cells}'
            'free cold cells and {free_freeze_cells} free freeze cells'.format(
                refr_type=type(self).__name__,
                refr_name=self.name,
                free_cold_cells=(self.capacity['cold'] -
                                 self.occupied_cells['cold']),
                free_freeze_cells=(self.capacity['freeze'] -
                                   self.occupied_cells['freeze'])))


class RefrigeratorAtlant(Refrigerator):
    """Belorussian refrigerator with small capacity"""
    made_in = 'Belarus'
    models_capacity = {'Minsk': {'freeze': 4, 'cold': 6},
                       'Lider': {'freeze': 3, 'cold': 2}}


class RefrigeratorPhillips(Refrigerator):
    """High quality netherlands refrigerator with meddle capacity"""
    made_in = 'The Netherlands'
    models_capacity = {'model A': {'freeze': 6, 'cold': 12},
                       'model B': {'freeze': 7, 'cold': 14},
                       'model C': {'freeze': 20, 'cold': 0}}


def example():
    RefrigeratorAtlant.create_or_update_model('Minsk', 5, 6)
    refr1 = RefrigeratorAtlant(name='Atlant M150', model='Minsk')
    refr1.display_info()
    mam = Parent('Olga')
    child1 = Child('Vitya')
    while not refr1.broken:
        child1.hit_fridge(refr1)
    master1 = Master(7)
    master1.study()
    master1.study()
    master1.advertisement()
    if refr1.broken:
        mam.call_to_master(master1, refr1)
    apple = Product('apple', size=3)
    meat = Product('meat', pr_type='freeze', size=2)
    mam.put_product(refr1, apple)
    mam.put_product(refr1, meat)
    refr1.display_info()
    mam.take_product(meat)
    refr1.display_info()
    mam.take_product(meat)


example()
