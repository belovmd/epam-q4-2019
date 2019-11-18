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

    def take_product(self, refr, product):
        """Method try to take product from refrigerator

        If refrigerator is broken or product not in it, we do nothing.
        Otherwise user take product, and cells we it lie become free.
        """
        if refr.broken:
            print('{} is broken!'.format(refr.name))
        else:
            if product.in_freeze_cam == refr:
                refr.freeze_cells -= product.size
                product.in_freeze_cam = None
            elif product.in_cold_cam == refr:
                refr.cold_cells -= product.size
                product.in_cold_cam = None
            else:
                print('{0} is not in {1}.{2} still hungry'.format(product.name,
                                                                  refr.name,
                                                                  self.name))

    def put_product(self, refr, product):
        """Method try to put product in refrigerator

        If refrigerator is broken or product is already in refrigerator, we do
        nothing.

        Otherwise if it is "cold", we tried to find place for it in cold camera
        If it it's not enough place in cold camera or it is freeze product,
        we tried to put product in freeze camera.
        If it it's not enough place in freeze camera, we will not put product
        in refrigerator.
        """
        if refr.broken:
            print('{} is broken!'.format(refr.name))
        elif product.in_cold_cam == refr or product.in_freeze_cam == refr:
            print('{} is already in {}!'.format(product.name, refr.name))
        else:
            if product.pr_type == 'cold' and (refr.cold_cells + product.size <=
                                              refr.cold_cam_capacity):
                product.in_cold_cam = refr
                refr.cold_cells += product.size
            elif refr.freeze_cells + product.size <= refr.freeze_cam_capacity:
                product.in_freeze_cam = refr
                refr.freeze_cells += product.size
            else:
                print('{0} can\'t put {1} in {2} - not enough place!'
                      .format(self.name, product.name, refr.name))

    def eat(self, product):
        """If product is in refrigerator, in will be deleted forever"""
        if not product.in_freeze_cam or not product.in_cold_cam:
            print('{} can\'t eat product from refrigerator!'.format(self.name))
        else:
            print('{} eat {}'.format(self.name, product.name))
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
        print('{} called to {}.'.format(self.name, master.name), end=' ')
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
            print('{} broke {}!'.format(self.name, refr.name))
        else:
            print('{} hit {}, but not broke.'.format(self.name, refr.name))


class Master(object):
    """Master is a person who can fix refrigerators if he have enough skill"""
    money = 100

    def __init__(self, skill, name='Master', company='own'):
        self.skill = skill
        self.name = name
        self.company = company

    def advertisement(self):
        """Advertising of master. Skills always increase by two"""
        print('Highly skilled master {0} from {1} company is looking for work!'
              ' My skill is {2}. Prices:\nImport refrigerator: {3}\nDomestic '
              'refrigerator: {4}'.format(self.name, self.company,
                                         str(self.skill + 2),
                                         str(self.skill * 150),
                                         str(self.skill * 100)))

    def try_to_fix(self, customer, refr):
        """Master will try to fix refrigerator

        Price formula: skill * 100 * сoeff
        Netherlands refrigerators can be fixed by only masters with >=7 skill,
        coeff is 1,5
        Belarus refrigerators can be fixed only by masters with >=3 skill,
        coeff is 1, and also help to improve some skills.
        Payment is made by the client (Parent)
        Сonsultation is free.
        """
        if refr.made_in == 'The Netherlands':
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
        """Master can pay money and improve his skills"""
        if self.money >= 100:
            self.money -= 100
            self.skill += 1
        else:
            print('{self.master} don\'t have enough money to study')


class Product(object):
    """Product is some food we can eat or put to refrigerator

    It can be cold and freeze type.
    Every product aso have size -oit shows how many cells this product need
    """
    in_cold_cam = None
    in_freeze_cam = None

    def __init__(self, name, pr_type='cold', size=1):
        self.name = name
        self.pr_type = pr_type
        self.size = size


class Refrigerator(object):
    """Refrigerator is place where we can save products

    New refrigerator always is empty and able to work
    """
    freeze_cells = 0
    cold_cells = 0
    broken = False

    def __init__(self, name):
        self.name = name

    def display_info(self):
        """Show information about refrigerator and free cells"""
        print('Hi, I am {0} aka {1}\nNow it is {2} free cold cells'
              ' and {3} free freeze cells '.format(type(self).__name__,
                                                   self.name,
                                                   self.cold_cells,
                                                   self.freeze_cells))


class RefrigeratorAtlant(Refrigerator):
    """Belorussian refrigerator with small capacity"""
    made_in = 'Belarus'
    freeze_cam_capacity = 4
    cold_cam_capacity = 6


class RefrigeratorPhillips(Refrigerator):
    """High quality netherlands refrigerator with meddle capacity"""
    made_in = 'The Netherlands'
    freeze_camera_capacity = 6
    cold_camera_capacity = 12


def example():
    refr1 = RefrigeratorAtlant('Atlant M150')
    mam = Parent('Olga')
    child1 = Child('Vitya')
    while not refr1.broken:
        child1.hit_fridge(refr1)
    master1 = Master(7)
    master1.advertisement()
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


example()
