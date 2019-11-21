"""This function adds an element to a list inside a dict of lists. Rewrite
it to use a try-except statement which handles a possible KeyError if the
list with the name provided doesn't exist in the dictionary yet, instead of
checking beforehand whether it does. Include else and finally clauses in
your try-except block."""


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)

    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname))


if __name__ == '__main__':
    months = {1: ["January"], 3: ["March"], 4: ["April"], 5: ["May"],
              6: ["June"], 7: ["July"], 8: ["August"], 9: ["September"],
              10: ["October"], 11: ["November"], 12: ["December"]}
    add_to_list_in_dict(months, 3, "M?rz")
    add_to_list_in_dict(months, 2, "February")
    add_to_list_in_dict(months, 2, "Februar")
