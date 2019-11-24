""" Create unit tests for any program from previous homeworks.
Code coverage has to be >= 80% """

import tested_module
import unittest


class TestModule(unittest.TestCase):
    def test_generate_numbers(self):
        self.assertEqual(tested_module.generate_numbers(2), {1: 1, 2: 4})

    def test_count_characters(self):
        self.assertEqual(tested_module.count_characters('ab'), {'a': 1, 'b': 1})

    def test_list_1(self):
        self.assertEqual(tested_module.list_1[1], 'ac')

    def test_list_2(self):
        self.assertTrue(tested_module.list_2[2] == 'bc')

    def test_list_3(self):
        self.assertFalse(tested_module.list_3[0] == '1b')

    def test_index(self):
        with self.assertRaises(IndexError):
            tested_module.list_1t[3]

    def test_tuples(self):
        self.assertIsNot(tested_module.tuple_1, tested_module.tuple_2)

    def test_not_empty(self):
        self.assertIsNotNone(tested_module.list_2t)

    def test_instantiations(self):
        a, b, c = tested_module.a, tested_module.b, tested_module.c
        self.assertNotEqual((a, b, c), ('a', 3, 'gamma'))


if __name__ == "__main__":
    unittest.main()
