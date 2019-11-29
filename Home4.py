import math
import time


# task 1
def wrapper(f):
    def res(*args, **kwargs):
        t0 = time.time()
        res = f(*args, **kwargs)
        t1 = time.time()
        result.append(res)
        delta_time = t1 - t0
        time_result.append(delta_time)
        return result, time_result

    return res


@wrapper
def func(x, y):
    return x ** y


# task 2
def get_ranges(int_list):
    output = []
    start_position = 0
    current_position = 0
    while start_position != len(int_list):
        while current_position < len(int_list) - 1 \
                and int_list[current_position] + 1 == int_list[current_position + 1]:
            current_position += 1
        if start_position == current_position:
            output.append(str(int_list[current_position]))
        else:
            output.append(str(int_list[start_position]) + "-" +
                          str(int_list[current_position]))
        current_position += 1
        start_position = current_position
    print(output)


# Codewars task
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
def generate_hashtag(strng):
    if strng == '':
        return False
    else:
        hashtag = '#'
        strng = list(strng)
        strng[0] = strng[0].upper()
        i = 1
        while i != len(strng):
            if strng[i - 1] == ' ':
                strng[i] = strng[i].upper()
            else:
                strng[i] = strng[i].lower()
            i += 1
        x = 0
        strng1 = ''
        while x != len(strng):
            strng1 += str(strng[x])
            x += 1
        strng1 = strng1.replace(' ', '')
        if strng1[0] == '#':
            pass
        else:
            hashtag = hashtag + strng1
        if len(hashtag) > 140:
            return False
        else:
            return hashtag


# https://files.fm/f/qbw4a8gb
# please, check this strange formula,
# which was created for some scientific purposes
# here is it's Python realization
def angle_inaccuracy(a, b, c, inaccuracy):
    v1 = a ** 2 / (b ** 2 * c ** 2)
    v2 = (a ** 2 + b ** 2 - c ** 2) ** 2 / (4 * b ** 4 * c ** 2)
    v3 = (a ** 2 - b ** 2 + c ** 2) ** 2 / (4 * b ** 2 * c ** 4)
    v4 = (4 * b ** 2 * c ** 2 - (b ** 2 + c ** 2 - a ** 2) ** 2) \
         / (4 * b ** 2 * c ** 2)
    formula = (v1 + v2 + v3) / v4
    delta_alpha = math.sqrt(formula) * inaccuracy
    r_file = math.degrees(delta_alpha)
    print(r_file)
    return r_file
