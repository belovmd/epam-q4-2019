"""This function adds an element to a list inside
a dict of lists. Rewrite it to use a try-except
statement which handles a possible KeyError if
the list with the name provided doesn’t exist
in the dictionary yet, instead of checking
beforehand whether it does. Include else
and finally clauses in your try-except block:
"""


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


if __name__ == '__main__':
    test_dict = {'one': [1, 2, 3], 'two': [1, 2, 3]}
    add_to_list_in_dict(thedict=test_dict, listname='one', element=4)
    add_to_list_in_dict(thedict=test_dict, listname='three', element=5)
    print(test_dict)
