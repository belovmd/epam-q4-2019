#!/usr/bin/env python3.7

"""Conclusion message to the grocer about the debt of the buyer.

7 lines: Dictionaries, generator expressions
from https://wiki.python.org/moin/SimplePrograms .

"""

PRICES = {'apple': 0.40, 'banana': 0.50}
MY_PURCHASE = {
    'apple': 1,
    'banana': 6}
GROCERY_BILL = sum(PRICES[idx] * MY_PURCHASE[idx]
                   for idx in MY_PURCHASE)
print('I owe the grocer $%.2f' % GROCERY_BILL)
