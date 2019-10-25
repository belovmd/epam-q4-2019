#!/usr/bin/env python3.7

"""Output list fibonacci with mask.

mask: "This generation has {fibonacchi_number} babies".

4 lines: Fibonacci, tuple assignment
from https://wiki.python.org/moin/SimplePrograms .

"""

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
