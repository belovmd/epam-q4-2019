import unittest


# task 1.1
def divider(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('DivisionError')


divider(5, 0)


# task 1.2
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print('Index Error')


print_list_element([1, 2, 3], 5)


# task 1.3
def add_to_list_in_dict(thedict, listname, element):
    try:
        curr_list = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(curr_list)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))
    return thedict


# task 3
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(
            add_to_list_in_dict({'key1': [1, 2], 'key2': [4]}, 'new_k', 8),
            {'key1': [1, 2], 'key2': [4], 'new_k': [8]})


if __name__ == '__main__':
    unittest.main()
