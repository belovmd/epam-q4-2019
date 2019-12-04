"""Simulator from real life medical drug selling.

Simulated objects contain attributes and methods to simulate some use cases.
Program prints objects' states, methods and interaction.
"""

import types


class DecoMeta(type):
    def __new__(mcs, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, types.FunctionType):
                attrs[attr_name] = mcs.deco(attr_value)

        return super(DecoMeta, mcs).__new__(mcs, name, bases, attrs)

    @classmethod
    def deco(cls, func):
        def wrapper(*args, **kwargs):
            print("before", func.__name__)
            for arg in args:
                if not isinstance(arg, (str, int)):
                    print(arg, 'state:', str(arg.__dict__))
            result = func(*args, **kwargs)
            print("after", func.__name__)
            for arg in args:
                if not isinstance(arg, (str, int)):
                    print(arg, 'state:', str(arg.__dict__))
            return result
        return wrapper


class Pharmacy(metaclass=DecoMeta):

    def __init__(self, is_open=False, drugs={"my_medicine": 0}, cash=0):
        self.is_open = is_open
        self.drugs = drugs
        self.cash = cash


class Pharmaceutist(metaclass=DecoMeta):

    def __init__(self, pharmacy):
        self.pharmacy = pharmacy
        self.drug = None

    def open_pharmacy(self):
        self.pharmacy.is_open = True

    def close_pharmacy(self):
        self.pharmacy.is_open = True

    def get_drugs(self, drug_name="my_medicine", drug_count=1):
        if drug_name in self.pharmacy.drugs:
            self.pharmacy.drugs[drug_name] += drug_count
        else:
            self.pharmacy.drugs[drug_name] = drug_count

    def check_prescripton(self, customer):

        if customer.prescription:
            self.drug = customer.prescription

    def take_money(self, customer):
        medicine_cost = 1
        customer.money -= medicine_cost
        self.pharmacy.cash += medicine_cost

    def give_drugs(self, customer):
        self.pharmacy.drugs[self.drug] -= 1
        customer.drugs = {self.drug: 1}


class Customer(metaclass=DecoMeta):

    def __init__(self, prescription, money):
        self.prescription = prescription
        self.money = money
        self.drugs = {}


my_pharmacy = Pharmacy()
my_pharmaceutist = Pharmaceutist(my_pharmacy)

my_first_customer = Customer(prescription='my_medicine', money=100)
my_pharmaceutist.open_pharmacy()
my_pharmaceutist.get_drugs()
my_pharmaceutist.check_prescripton(my_first_customer)
my_pharmaceutist.take_money(my_first_customer)
my_pharmaceutist.give_drugs(my_first_customer)

my_second_customer = Customer(prescription='another_medicine', money=66)
my_pharmaceutist.get_drugs('another_medicine', 5)
my_pharmaceutist.check_prescripton(my_second_customer)
my_pharmaceutist.take_money(my_second_customer)
my_pharmaceutist.give_drugs(my_second_customer)

###

my_pharmaceutist.close_pharmacy()
