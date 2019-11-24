from Task1 import add_to_list_in_dict
import unittest


class TestFunction(unittest.TestCase):

    def test_add_to_list_in_dict_case1(self):
        dct1 = {"1": [1]}
        add_to_list_in_dict(dct1, "1", 2)
        dct2 = {"1": [1, 2]}
        self.assertDictEqual(dct1, dct2)

    def test_add_to_list_in_dict_case2(self):
        dct1 = {"1": [1]}
        add_to_list_in_dict(dct1, "2", 3)
        dct2 = {"1": [1],
                "2": [3]}
        self.assertEqual(dct1, dct2)


if __name__ == "__main__":
    unittest.main()
