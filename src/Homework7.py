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

# Sorry, have problems with installing nosetest on windows at this moment,
# I will add this task later
# 3 Cover function from 1.3 with tests


class MyTestFunction(unittest.TestCase):

    def test_add_without_list(self):
        legends_1 = {'Beatles': ['John_lennon'],
                     'Rolling_Stones': ['Mick_Jagger'],
                     'Deep_Purple': ['Ian_Gillan'],
                     'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        add_to_list_in_dict(legends_1, 'Queen', 'Freddie_Mercury')
        legends_2 = {'Beatles': ['John_lennon'],
                     'Rolling_Stones': ['Mick_Jagger'],
                     'Deep_Purple': ['Ian_Gillan'],
                     'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page'],
                     'Queen': ['Freddie_Mercury']}
        self.assertDictEqual(legends_1, legends_2)

    def test_add_with_list(self):
        legends_1 = {'Beatles': ['John_lennon'],
                     'Rolling_Stones': ['Mick_Jagger'],
                     'Deep_Purple': ['Ian_Gillan'],
                     'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        add_to_list_in_dict(legends_1, 'Beatles', 'Ringo_Starr')
        legends_2 = {'Beatles': ['John_lennon', 'Ringo_Starr'],
                     'Rolling_Stones': ['Mick_Jagger'],
                     'Deep_Purple': ['Ian_Gillan'],
                     'Led_Zeppelin': ['Robert_Plant', 'Jimmy_Page']}
        self.assertDictEqual(legends_1, legends_2)


if __name__ == '__main__':
    unittest.main()
