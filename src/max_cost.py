'''Find max value in dict'''


def max_cost(dict_):
    return max(dict_.items(), key=lambda x: x[-1])


if __name__ == '__main__':
    print(*max_cost({'CAC': 10, 'ATX': 390, 'WIG': 1.2}))
