#!/usr/bin/env python3.7

"""Output constant friends list.

3 lines: For loop, built-in enumerate function, new style
formatting from https://wiki.python.org/moin/SimplePrograms .

"""

FRIENDS = ['john', 'pat', 'gary', 'michael']
for idx, friend in enumerate(FRIENDS):
    print("iteration {iteration} is {friend}"
          .format(iteration=idx, friend=friend))
