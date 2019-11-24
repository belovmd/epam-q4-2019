"""Homework 7 - 1. Exception practice"""


# Write a function to compute 5/0 and use try/except to catch the
# DivisionError exception.
def division():
    try:
        5 / 0
    except ZeroDivisionError as exc:
        print(exc)


# Add a try-except statement to the body of this function which handles
# a possible IndexError, which could occur if the index provided exceeds
# the length of the list. Print an error message if this happens
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as exc:
        print(exc)


# This function adds an element to a list inside a dict of lists.
# Rewrite it to use a try-except statement which handles a possible KeyError
# if the list with the name provided doesn’t exist in the dictionary yet,
# instead of checking beforehand whether it does.
# Include else and finally clauses in your try-except block
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
