"""This function adds an element to a list inside a dict of lists. Rewrite it
to use a try-except statement which handles a possible KeyError if the list
with the name provided doesn’t exist in the dictionary yet, instead of
checking beforehand whether it does. Include else and finally clauses in your
try-except block.
"""


def add_to_list_in_dict(thedict, listname, element):
    try:
        try:
            lst = thedict[listname]
        except TypeError:
            raise TypeError("Input correct arguments.")
        print("%s already has %d elements." % (listname, len(lst)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
        thedict[listname].append(element)
    else:
        thedict[listname].append(element)
    finally:
        print("Added %s to %s." % (element, listname))
    return thedict


if __name__ == '__main__':
    dct = {'a': [1, 2, 3], 'b': [], 'c': ['sss', 'sds']}
    add_to_list_in_dict(dct, 'a', 77)
    add_to_list_in_dict(dct, 'x', 12)
