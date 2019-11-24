"""This function adds an element to a list inside a dict of lists. Rewrite it
to use a try-except statement which handles a possible KeyError if the list
with the name provided doesn’t exist in the dictionary yet, instead of
checking beforehand whether it does. Include else and finally clauses in your
try-except block.
"""


def add_to_list_in_dict(thedict, listname, element):
    try:
        lst = thedict[listname]
        print("%s already has %d elements." % (listname, len(lst)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("Added %s to %s." % (element, listname))
    finally:
        thedict[listname].append(element)


if __name__ == '__main__':
    dct = {'a': [1, 2, 3], 'b': [], 'c': ['sss', 'sds']}
    add_to_list_in_dict(dct, 'a', 77)
    print(dct)
    add_to_list_in_dict(dct, 'x', 12)
    print(dct)
