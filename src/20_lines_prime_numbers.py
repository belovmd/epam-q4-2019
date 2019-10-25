#!/usr/bin/env python3.7

"""Prime numbers sieve w/fancy generators.

20 lines: Prime numbers sieve w/fancy generators
from https://wiki.python.org/moin/SimplePrograms .

"""

import itertools


def iter_primes():
    """Iterate all prime numbers between 2 and +infinity."""
    numbers = itertools.count(2)

    # generate primes forever
    while True:
        # get the first number from the iterator (always a prime)
        prime = next(numbers)
        yield prime

        # this code iteratively builds up a chain of
        # filters...slightly tricky, but ponder it a bit
        numbers = filter(prime.__rmod__, numbers)


for p in iter_primes():
    if p > 1000:
        break
    print(p)
