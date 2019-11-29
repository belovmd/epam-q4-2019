"""
Rewrite it to use a try-except
statement which handles a possible KeyError
if the list with the name provided doesn’t exist
in the dictionary yet, instead of checking beforehand
whether it does. Include else and finally
clauses in your try-except block:
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

dict1 = {1: [556]}


