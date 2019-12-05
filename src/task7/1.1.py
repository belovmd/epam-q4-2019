
def devision(number, divisor):

    try:
        return number / divisor
    except ZeroDivisionError as e:
        return e


if __name__ == '__main__':
    print(devision(5, 2))
    print(devision(5, 0))
