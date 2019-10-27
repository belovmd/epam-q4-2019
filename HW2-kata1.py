""" 5 kyu - Moving Zeros To The End
https://www.codewars.com/kata/52597aa56021e91c93000cb0

Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    array_without_zero = [i for i in array if (i != 0) or (type(i) == bool)]
    new_array = array_without_zero + [0]*(len(array) - len(array_without_zero))
    return new_array


print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))  # for example
