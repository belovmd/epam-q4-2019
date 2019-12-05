
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    print_list_element([1, 2, 3, 4, 5, 6, 7], 3)
    print_list_element([1, 2, 3, 4, 5, 6, 7], 10)
