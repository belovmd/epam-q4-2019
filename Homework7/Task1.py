""" 1.1 Write a function to compute 5/0 and use try/except to catch
the DevisionError exception. """


def five_zero():
    try:
        5 / 0
    except ZeroDivisionError:
        print('No result')


""" 1.2 Add a try-except statement to the body of this function which handles
a possible IndexError, which could occur if the index provided exceeds the
length of the list. Print an error message if this happens:
def print_list_element(thelist, index):
    print(thelist[index]) """


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as err:
        print(err)


""" 1.3 This function adds an element to a list inside a dict of lists.
Rewrite it to use a try-except statement which handles a possible KeyError
if the list with the name provided doesn’t exist in the dictionary yet,
instead of checking beforehand whether it does. Include else and finally
clauses in your try-except block:
def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        ll = thedict[listname]
        print("%s already has %d elements." % (listname, len(ll)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)
    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname)) """


def add_to_list_in_dict(thedict, listname, element):
    try:
        ll = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(ll)))
    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname))
