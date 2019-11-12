# lists
# 1 Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list1_1 = [let1 + let2 for let1 in 'ab' for let2 in 'bcd']
print(list1_1)
# 2 Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
list1_2 = list1_1[0:2]
print(list1_2)
# 3 Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
list1_3 = [str(let + 'a') for let in '1234']
print(list1_3)
# 4 Simultaneously remove the element '2a' from the above list and print it.
print(list1_3.pop(1))
# 5 Copy the above list and add '2a' back into the list
# such that the original is still missing it.
list1_5 = list1_3.copy()
list1_5.insert(1, '2a')
print(list1_5)

# tuples
# 1 Create the list ['a', 'b', 'c'], then create a tuple from that list.
list2_1 = ['a', 'b', 'c']
tuple2_1 = tuple(list2_1)
print(tuple2_1)
# 2 Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
tuple2_2 = ('a', 'b', 'c')
print(tuple2_2)
list2_2 = list(tuple2_2)
print(list2_2)
# 3 Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'.
# (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print("a =", a, ", b =", b, ", c =", c)
# 4 Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.
tuple2_4 = (('a', 'b', 'c'),)
print(len(tuple2_4))
print(tuple2_4[0])


# dictionaries
# 1 Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included) and the values are
# square of keys. n – function argument. Default is 20.
def generate_numbers(n=20):
    """generate dictionary {number: square of a number}"""
    dict3_1 = {i + 1: pow(i + 1, 2) for i in range(n)}
    return dict3_1


print(generate_numbers(5))
print(generate_numbers())


# 2 Define a function count_characters(count_me_string)
# which count and return the numbers of each character 
# in a count_me_string argument.
def count_characters(count_me):
    """count the number of characters in the string (case non-sensitive)"""
    dict3_2 = {}
    for let in count_me.lower():
        if let in dict3_2:
            dict3_2[let] += 1
        else:
            dict3_2[let] = 1
    return dict3_2


print(count_characters('abcDEFgAbc'))
