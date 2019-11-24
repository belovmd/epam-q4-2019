"""Write a function to compute 5/0 and use try/except to catch the
DivisionError exception.
"""


def division_by_zero():
    """Function computes 5/0 and catches the DivisionError exception"""
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print('You cannot divide by 0')


division_by_zero()
