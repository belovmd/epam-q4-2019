"""
Реализовать функцию get_ranges 
которая получает на вход непустой список 
неповторяющихся целых чисел,
отсортированных по возрастанию,
которая этот список “сворачивает”
"""


def get_ranges(line):
    new_line = ""
    for i in range(len((line)) - 1):
        if line[i] + 1 != line[i + 1]:
            new_line += str(line[i]) + "," 
        elif line[i] - 1 != line[i - 1]:
            new_line += str(line[i]) + "-"     
    new_line += str(line[-1])        
    return new_line

  
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # "0-4,7-8,10"
print(get_ranges([4, 7, 10]))  # "4,7,10"
print(get_ranges([2, 3, 8, 9]))  # "2-3,8-9"