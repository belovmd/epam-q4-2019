"""Purchase money calculation."""


import re
PATTERN_CENTS = re.compile("^[0-9]{0,2}$")
PATTERN_INT = re.compile("^[0-9]*$")


print('{:#^100}'.format('Start programm'))
parametr_pass_flag = False
print('{:*^100}'.format('Start inputing'))

while not parametr_pass_flag:
    print("Input cost of product")
    cents = input("Cents: ")
    dollars = input("Dollars: ")
    count_items = input("Count items: ")
    parametr_pass_flag = PATTERN_INT.match(dollars) and \
        PATTERN_INT.match(count_items) and \
        PATTERN_CENTS.match(cents)

print('{:*^100}'.format('End inputing cost of product'))

print("Result: " + str((int(dollars) + int(cents) / 100) * int(count_items)))
print('{:#^100}'.format('End programm'))
