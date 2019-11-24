"""Write a function to compute 5/0 and use try/except
to catch the DevisionError exception.
"""


def division_by_zero():
    try:
        return 5 / 0
    except ZeroDivisionError as error:
        print('Error:' + str(error))


if __name__ == '__main__':
    division_by_zero()
