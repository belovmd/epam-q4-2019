# 1.1 Write a function to compute 5/0 and use try/except to catch
# the DivisionError exception.
import unittest

try:
    result = 5 / 0
except ZeroDivisionError as div0error:
    print('Что-то пошло не так...: ' + str(div0error))


# 1.2 Add a try-except statement to the body of this function which handles
# a possible IndexError, which could occur if the index provided exceeds the
# length of the list. Print an error message if this happens.


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as error:
        print(str(error))


list7_2 = [x for x in range(10) if x % 2 == 0]
print_list_element(list7_2, 6)


# 1.3 This function adds an element to a list inside a dict of lists. Rewrite
# it to use a try-except statement which handles a possible KeyError if the
# list with the name provided doesn't exist in the dictionary yet, instead of
# checking beforehand whether it does. Include else and finally clauses in
# your try-except block.


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


legends = {'Beatles': ['John_lennon'], 'Rolling_Stones': ['Mick_Jagger'],
           'Deep_Purple': ['Ian_Gillan']}
add_to_list_in_dict(legends, 'Led_Zeppelin', 'Robert_Plant')
add_to_list_in_dict(legends, 'Led_Zeppelin', 'Jimmy_Page')
print(legends)

# 2  Create unit tests for any program from previous homeworks.
# Use http://nose.readthedocs.io/en/latest/ to run tests.
# Code coverage has to be >= 80%
# http://nose.readthedocs.io/en/latest/plugins/cover.html
# Sorry, have problems with installing nosetest on windows, so i covered
#  a "palindrome" function with unitest instead
# 3 Cover function from 1.3 with tests


def palindrome(input_number):
    try:
        input_number = int(input_number)
    except ValueError as error:
        print("Error", error)
        return
    original_num = input_number
    ostatok = 0
    reversd_num = 0
    while input_number != 0:
        ostatok = input_number % 10
        reversd_num = reversd_num * 10 + ostatok
        input_number = input_number // 10
    if original_num != reversd_num:
        return False
    return True


class MyTestFunction(unittest.TestCase):

    def test_not_a_palindrome(self):
        self.assertEqual(palindrome('126898721'), False)

    def test_is_a_palindrome(self):
        self.assertEqual(palindrome('256343652'), True)

    def test_not_valid_number(self):
        self.assertEqual(palindrome('985l589'), None)

    def test_add_without_list(self):
        original_dict = {'Beatles': ['John_lennon'],
                         'Rolling_Stones': ['Mick_Jagger'],
                         'Deep_Purple': ['Ian_Gillan'],
                         'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        add_to_list_in_dict(original_dict, 'Queen', 'Freddie_Mercury')
        expected_dict = {'Beatles': ['John_lennon'],
                         'Rolling_Stones': ['Mick_Jagger'],
                         'Deep_Purple': ['Ian_Gillan'],
                         'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page'],
                         'Queen': ['Freddie_Mercury']}
        self.assertDictEqual(original_dict, expected_dict)

    def test_add_with_list(self):
        original_dict = {'Beatles': ['John_lennon'],
                         'Rolling_Stones': ['Mick_Jagger'],
                         'Deep_Purple': ['Ian_Gillan'],
                         'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        add_to_list_in_dict(original_dict, 'Beatles', 'Ringo_Starr')
        expected_dict = {'Beatles': ['John_lennon', 'Ringo_Starr'],
                         'Rolling_Stones': ['Mick_Jagger'],
                         'Deep_Purple': ['Ian_Gillan'],
                         'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        self.assertDictEqual(original_dict, expected_dict)

    def test_add_with_empty_dict(self):
        original_dict = {}
        add_to_list_in_dict(original_dict, 'Queen', 'Freddie_Mercury')
        expected_dict = {'Queen': ['Freddie_Mercury']}
        self.assertDictEqual(original_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
