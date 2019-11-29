from calculator import Calculator
from chef import Chef
from cucumber import Cucumber
from onion import Onion
from tomato import Tomato
import unittest


class CalculatorTest(unittest.TestCase):

    product1 = Cucumber(10, 10, 10)
    product2 = Onion(5, 5, 'red')
    product3 = Tomato(20, 10, 'gniloy')

    ingridients1 = [product1, product2, product3]
    ingridients2 = []

    chef1 = Chef("Raf", ingridients1)
    chef2 = None
    chef3 = Chef("Vasil", ingridients2)
    print(chef1)
    def test_total_weight_salt1_is_35(self):
        exp_result = 35
        result = Calculator.total_weight_salt(self.chef1)
        self.assertEqual(exp_result, result)

    def test_total_weight_salt2_is_0(self):
        exp_result = 0
        result = Calculator.total_weight_salt(self.chef3)
        self.assertEqual(exp_result, result)

    def test_total_weight_if_chef_is_None(self):
        exp_result = 0
        result = Calculator.total_weight_salt(self.chef2)
        self.assertEqual(exp_result, result)

    def test_total_calories_salt1_is_25(self):
        exp_result = 25
        result = Calculator.total_calories_salt(self.chef1)
        self.assertEqual(exp_result, result)

    def test_total_calories_if_chef_is_None(self):
        exp_result = 0
        result = Calculator.total_calories_salt(self.chef2)
        self.assertEqual(exp_result, result)

    def test_total_calories_salt2_is_0(self):
        exp_result = 0
        result = Calculator.total_calories_salt(self.chef3)
        self.assertEqual(exp_result, result)
