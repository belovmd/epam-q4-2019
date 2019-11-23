"""Write a function to compute 5/0 and use try/except to catch the
 DevisionError exception."""


def division(first_digit, second_digit):
    try:
        return first_digit / second_digit
    except ZeroDivisionError as exc:
        return str(exc)


"""Add a try-except statement to the body of this function which handles a
possible IndexError, which could occur if the index provided exceeds the
length of the list. Print an error message if this happens."""


def print_list_element(list_, index):
    try:
        return list_[index]
    except IndexError as exc:
        return str(exc)


"""This function adds an element to a list inside a dict of lists. Rewrite
it to use a try-except statement which handles a possible KeyError if the
list with the name provided doesn't exist in the dictionary yet, instead of
checking beforehand whether it does. Include else and finally clauses in
your try-except block."""


def add_to_list_in_dict(dict_, list_name, element):
    try:
        l = dict_[list_name]
    except KeyError:
        dict_[list_name] = []
    else:
        print('%s already has %d elements.' % (list_name, len(l)))
    finally:
        dict_[list_name].append(element)
        print('Added %s to %s' % (element, list_name))
        return dict_


if __name__ == '__main__':
    print(division(5, 0))
    print(print_list_element([1, 2, 5, 6, 7], 10))
    dct = {'digits': [digit for digit in range(5)]}
    add_to_list_in_dict(dct, 'digits', 10)
    add_to_list_in_dict(dct, 'digit', 10)
