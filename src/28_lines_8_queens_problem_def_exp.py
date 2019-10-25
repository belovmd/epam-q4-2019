#!/usr/bin/env python3.7

"""8-Queens Problem (define your own exceptions).

28 lines: 8-Queens Problem (define your own exceptions)
from https://wiki.python.org/moin/SimplePrograms .

"""

BOARD_SIZE = 8


class BailOut(Exception):
    """Exeption if me can't add queen."""


def validate(queens):
    """Validate opporutinity adding queen."""
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens):
    """Add queen on the board."""
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut


QUEENS = add_queen([])
print(QUEENS)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in QUEENS))
