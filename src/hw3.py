# lists
# 1
list1_1 = [let1 + let2 for let1 in 'ab' for let2 in 'bcd']
print(list1_1)
# 2
list1_2 = list1_1[0:5:2]
print(list1_2)
# 3
list1_3 = [str(i + 1) + 'a' for i in range(4)]
print(list1_3)
# 4
print(list1_3.pop(1))
# 5
list1_5 = list1_3.copy()
list1_5.insert(1, '2a')
print(list1_5)


# tuples
# 1
list2_1 = [let for let in 'abc']
tuple2_1 = tuple(list2_1)
print(tuple2_1)
# 2
tuple2_2 = ('a', 'b', 'c')
print(tuple2_2)
list2_2 = list(tuple2_2)
print(list2_2)
# 3
a, b, c = 'a', 2, 'gamma'
print("a =", a, ", b =", b, ", c =", c)
# 4
tuple2_4 = (('a', 'b', 'c'),)
print(len(tuple2_4))
print(tuple2_4[0])


# dictionaries
# 1
def generate_numbers(n=20):
    """generate dictionary {number: square of a number}"""
    dict3_1 = {}
    dict3_1.clear()
    i = 1
    while i <= n:
        dict3_1[i] = pow(i, 2)
        i += 1
    return dict3_1


print(generate_numbers(5))
print(generate_numbers())


# 2
# If we need to count 'a' and 'A' separately then remove the 'string' variable
# and use count_me in cycle both times instead
def count_characters(count_me):
    """count the number of characters in the string (case non-sensitive)"""
    dict3_2 = {}
    dict3_2.clear()
    pos = 0
    string = count_me.lower()
    while pos < len(count_me):
        dict3_2[string[pos:pos + 1]] = string.count(string[pos:pos + 1])
        pos += 1
    return dict3_2


print(count_characters('abcDEFgAbc'))
