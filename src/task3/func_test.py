import unittest
from func import add_to_list_in_dict


class Test_task13(unittest.TestCase):
    def test_add_1(self):
        d = {}
        add_to_list_in_dict(d, "list", 'element1')

        self.assertEqual(len(d.values()), 1)
        self.assertEqual(len(d['list']), 1)
        self.assertEqual(
            d,
            {'list': ['element1']})

    def test_add_2(self):
        d = {}
        add_to_list_in_dict(d, "list", 'element1')
        add_to_list_in_dict(d, "list", 'element2')

        self.assertEqual(len(d.values()), 1)
        self.assertEqual(len(d['list']), 2)
        self.assertEqual(
            d,
            {'list': ['element1', 'element2']})

    def test_add_3(self):
        d = {}
        add_to_list_in_dict(d, "list", 'element1')
        add_to_list_in_dict(d, "list", 'element2')
        add_to_list_in_dict(d, "list", 'element3')

        self.assertEqual(len(d.values()), 1)
        self.assertEqual(len(d['list']), 3)
        self.assertEqual(
            d,
            {'list': ['element1', 'element2', 'element3']})


if(__name__ == "__main__"):
    unittest.main()
