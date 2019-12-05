def add_to_list_in_dict(thedict, listname, element):
    try:
        lst = thedict[listname]
        print("%s already has %d elements." % (listname, len(lst)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


if __name__ == '__main__':
    add_to_list_in_dict({'foo': [1], 'bar': [2]}, 'baz', 3)
    add_to_list_in_dict({'foo': [1], 'bar': [2]}, 'bar', 3)
