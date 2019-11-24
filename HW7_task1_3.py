"""Task 1.3

This function adds an element to a list inside a dict of lists. Rewrite it
to use a try-except statement which handles a possible KeyError if the list
with the name provided doesnt exist in the dictionary yet, instead of
checking beforehand whether it does. Include else and finally clauses in
your try-except block:
"""


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
