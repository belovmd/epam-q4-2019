"""Create unit tests for any program from previous homeworks."""
import unittest


def count_characters(s='kappa'):
    """Function count and return the numbers of each character in a string."""
    dct = {}
    for symb in s:
        dct[symb] = dct.get(symb, 0) + 1
    return dct


class TestCountCharacters(unittest.TestCase):
    def test_normal(self):
        res = count_characters('coromilly')
        self.assertEqual(
            res, {'c': 1, 'o': 2, 'r': 1, 'm': 1, 'i': 1, 'l': 2, 'y': 1})

    def test_default_value(self):
        self.assertEqual(len(count_characters()), 3)

    def test_input_is_empty(self):
        res = count_characters('')
        self.assertEqual(res, {})

    def test_upper_lower(self):
        res = count_characters('cCC')
        self.assertEqual(res, {'c': 1, 'C': 2})

    def test_space(self):
        res = count_characters('one two')
        self.assertEqual(res,
                         {' ': 1, 'e': 1, 'n': 1, 'o': 2, 't': 1, 'w': 1})


if __name__ == '__main__':
    unittest.main()
