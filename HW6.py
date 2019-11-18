import random


class User(object):
    def __init__(self, name):
        self.name = name

    def take_product(self, refr, product):
        if refr.broken:
            print('{} is broken!'.format(refr.name))
        else:
            if product.in_freeze_cam:
                refr.freeze_cells -= product.size
                product.in_freeze_cam = False
            elif product.in_cold_cam:
                refr.cold_cells -= product.size
                product.in_cold_cam = False
            else:
                print('{0} is not in {1}.{2} still hungry'.format(product.name,
                                                                  refr.name,
                                                                  self.name))

    def put_product(self, refr, product):
        if refr.broken:
            print('{} is broken!'.format(refr.name))
        elif product.in_cold_cam or product.in_freeze_cam:
            print('{} os already in {}!'.format(product.name, refr.name))
        else:
            if product.pr_type == 'cold' and (refr.cold_cells + product.size <=
                                              refr.cold_cam_capacity):
                product.in_cold_cam = True
                refr.cold_cells += product.size
            elif refr.freeze_cells + product.size <= refr.freeze_cam_capacity:
                product.in_freeze_cam = True
                refr.freeze_cells += product.size
            else:
                print('{0} can\'t put {1} in {2} - not enough place!'
                      .format(self.name, product.name, refr.name))

    def eat(self, product):
        if product.in_freeze_cam or product.in_cold_cam:
            print('{} can\'t eat product from refrigerator!'.format(self.name))


class Parent(User):
    money = 1400

    def call_to_master(self, master, refr):
        job_result = master.try_to_fix(self, refr)
        print('{} called to {}.'.format(self.name, master.name), end=' ')
        print('He fixed it' if job_result else 'He can\'t fix it')

    def earn_money(self, salary=200):
        self.money += salary


class Child(User):
    def hit_fridge(self, refr):
        if random.random() < 0.35:
            refr.broken = True
            print('{} broke {}!'.format(self.name, refr.name))
        else:
            print('{} hit {}, but not broke.'.format(self.name, refr.name))


class Master(object):
    money = 100

    def __init__(self, skill, name='Master', company=None):
        self.skill = skill
        self.name = name
        self.company = company

    def try_to_fix(self, customer, refr):
        if refr.made_in == 'Netherlands':
            if self.skill >= 7:
                refr.broken = False
                customer.money -= self.skill * 100 * 1.5
                return True
        elif refr.made_in == 'Belarus':
            if self.skill >= 3:
                refr.broken = False
                customer.money -= self.skill * 100 * 1
                self.skill += 0.5
                return True
        return False

    def study(self):
        if self.money >= 100:
            self.money -= 100
            self.skill += 1
        else:
            print('{self.master} don\'t have enough money to study')


class Product(object):
    in_cold_cam = False
    in_freeze_cam = False

    def __init__(self, name, pr_type='cold', size=1):
        self.name = name
        self.pr_type = pr_type
        self.size = size


class Refrigerator(object):
    freeze_cells = 0
    cold_cells = 0
    broken = False

    def __init__(self, name):
        self.name = name

    def display_info(self):
        print('Hi, I am {0} aka {1}\nNow it is {2} free cold cells'
              ' and {3} free freeze cells '.format(type(self).__name__,
                                                   self.name,
                                                   self.cold_cells,
                                                   self.freeze_cells))


class RefrigeratorAtlant(Refrigerator):
    made_in = 'Belarus'
    freeze_cam_capacity = 4
    cold_cam_capacity = 6


class RefrigeratorPhillips(Refrigerator):
    made_in = 'Netherlands'
    freeze_camera_capacity = 6
    cold_camera_capacity = 12


def test():
    refr1 = RefrigeratorAtlant('Atlant M150')
    mam = Parent('Olga')
    child1 = Child('Vitya')
    while not refr1.broken:
        child1.hit_fridge(refr1)
    master1 = Master(7)
    if refr1.broken:
        mam.call_to_master(master1, refr1)
    apple = Product('apple', size=3)
    meat = Product('meat', pr_type='freeze', size=2)
    mam.put_product(refr1, apple)
    mam.put_product(refr1, meat)
    refr1.display_info()
    mam.take_product(refr1, meat)
    refr1.display_info()
    mam.take_product(refr1, meat)


test()
