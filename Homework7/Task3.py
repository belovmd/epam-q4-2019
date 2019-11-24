""" Cover function from 1.3 with tests. """

import unittest


def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        ll = thedict[listname]
        print("%s already has %d elements." % (listname, len(ll)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)
    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname))
    return thedict


class TestFunc(unittest.TestCase):
    def test_no_value(self):
        func = add_to_list_in_dict({'a': 1}, 'b', 'c')
        self.assertEqual(func, {'a': 1, 'b': ['c']})

    def test_value_int(self):
        with self.assertRaises(TypeError):
            add_to_list_in_dict({'a': 1}, 'a', 'c')

    def test_value_is(self):
        func = add_to_list_in_dict({'a': [1]}, 'a', 'c')
        self.assertTrue(func, {'a': [1, 'c']})

    def test_false(self):
        func = add_to_list_in_dict({'a': ['b']}, 'a', 'a')
        self.assertFalse(func == {'a': ['a', 'a']})

    def test_empty(self):
        self.assertIsNotNone(add_to_list_in_dict({}, 'a', 'a'))

    def test_len(self):
        func = add_to_list_in_dict({'a': ['b']}, 'c', 'd')
        self.assertNotEqual(len(func), 1)

    def test_key_value(self):
        func = add_to_list_in_dict({'a': ['b']}, 'c', 'd')
        self.assertEqual(func['c'], ['d'])


if __name__ == "__main__":
    unittest.main()
