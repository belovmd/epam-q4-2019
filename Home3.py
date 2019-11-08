"""List practice"""
lst = [ltr + ltr2 for ltr in "ab" for ltr2 in "bcd"]
lst = lst[::2]
new_list = ['1a', '2a', '3a', '4a']
new_list.pop(1)
list_copy = new_list.copy()
list_copy.insert(1, '2a')

# Tuple practice
lst = ['a', 'b', 'c']
tpl = tuple(lst)
lst_new = list(tpl)
a, b, c = 'a', 2, 'gamma'
tpl4 = ((a, b, c),)
print(len(tpl4))


# Dictionary practice
def generate_numbers(number=20):
    return {dct: dct ** 2 for dct in range(1, number + 1)}


def count_characters(count_me_string):
    return {dict_: count_me_string.count(dict_) for dict_ in count_me_string}
