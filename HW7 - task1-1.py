"""Task1.1

Write a function to compute 5/0 and use try/except to catch the
DivisionError exception.
"""


def try_to_divide(number1=5, number2=0):
    """Print result of division. If it is impossible - print reason"""

    try:
        print(number1 / number2)
    except ZeroDivisionError:
        print('You cannot divide by zero ')
    except TypeError:
        print('Please, use only two numbers')
