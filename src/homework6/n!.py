"""Algorithm with O(n!) complexity: Travelling salesman problem"""
import math
from numpy import array
from numpy import linalg
import random
import time


def create_city(max=50):
    return (random.randint(1, max + 1), random.randint(1, max + 1))


def generate_visit_order(number, length):
    order = []
    used = [i for i in range(1, length + 1)]
    for ptr in range(length):
        amount = math.factorial(length - 1 - ptr)
        element = math.floor(number // amount)
        order.append(used.pop(element))
        number -= element * amount
    return order


def add_route(cities, i):
    return linalg.norm(array(cities[i]) - array(cities[i - 1]))


def run(*args):
    for n in args:
        cities = []
        [cities.append(create_city()) for i in range(n)]
        res = 0
        start = time.time()
        for number in range(0, math.factorial(n) - 1):
            visit_order = generate_visit_order(number, n)
            curr_res = sum([add_route(cities, ptr - 1) for ptr in
                            visit_order])
            if not res or curr_res < res:
                res = curr_res
        if n == 2:
            res /= 2
        end = time.time()
        print("For {} cities result is {} and time is {} Cities: {}".format(
            n, res, end - start, cities))
        print("time / n! is {}\n".format((end - start) / math.factorial(n)))


if __name__ == '__main__':
    # run on different city numbers
    run(4, 5, 6, 7, 8)
