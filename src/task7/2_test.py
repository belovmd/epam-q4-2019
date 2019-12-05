from digits_multiplication import checkio
import unittest


class CheckioTest(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(checkio(123405), 120)
        self.assertEqual(checkio(67867), 14112)
        self.assertEqual(checkio(0000), 1)

    def test_empty(self):
        with self.assertRaises(TypeError):
            checkio()

    def test_invalid(self):
        with self.assertRaises(ValueError):
            checkio('sdsdsds')


if __name__ == '__main__':
    unittest.main()
