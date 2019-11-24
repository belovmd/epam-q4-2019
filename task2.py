"""Create unit tests for any program from previous homeworks."""
import unittest


def count_characters(s):
    """Function count and return the numbers of each character in a string."""
    dct = {}
    for symb in s:
        dct[symb] = dct.get(symb, 0) + 1
    return dct


class TestCountCharacters(unittest.TestCase):
    def test_normal(self):
        res = count_characters('coromilly')
        self.assertEqual(res, {'c': 1, 'o': 2, 'r': 1, 'm': 1, 'i': 1, 'l': 2, 'y': 1})

    def test_upper(self):
        self.assertEqual('coromilly'.upper(), 'COROMILLY')

    def test_lower(self):
        self.assertEqual('cOroMILly'.lower(), 'coromilly')

    def test_type(self):
        self.assertTrue(type('coromilly') is str)
        self.assertFalse(type(12345) is str)
        self.assertTrue(type({}) is dict)


if __name__ == '__main__':
    unittest.main()
