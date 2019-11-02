"""Fibonachi stream.

You're going to provide a needy programmer a utility method
that generates an infinite sized, sequential IntStream
(in TypeScript Iterator<number>, in Python generator)
which contains all the numbers in a fibonacci sequence.
"""


def all_fibonacci_numbers():
    """Fibonachi stream."""
    value, next_value = 1, 1
    while True:
        yield value
        value, next_value = next_value, value + next_value
