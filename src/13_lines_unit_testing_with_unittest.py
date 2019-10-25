#!/usr/bin/env python3.7

"""Unit testing with unittest.

13 lines: Unit testing with unittest
from https://wiki.python.org/moin/SimplePrograms .

"""

import unittest


def median(pool):
    """Return median off pull numbers."""
    copy = sorted(pool)
    size = len(copy)
    if size % 2 == 1:
        return copy[int((size - 1) / 2)]
    return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2


class TestMedian(unittest.TestCase):
    """Unit test median function."""

    def test_median(self):
        """Test median function."""
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7)


if __name__ == '__main__':
    unittest.main()
