def add_to_list_in_dict(thedict, listname, element):
    """Add element to list inside dictionary."""

    try:
        thedict[listname].append(element)
    except KeyError:
        thedict[listname] = []
        thedict[listname].append(element)
        print("Created {}.".format(listname))
    else:
        print("Total count in {}: {} elements.".format(
            listname,
            len(thedict[listname])))
    finally:
        print("Added {} to {}.".format(element, listname))


d = {}
add_to_list_in_dict(d, "list", 'element1')
print(d)
