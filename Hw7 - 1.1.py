"""
Write a function to compute 5/0
and use try/except to catch
the DevisionError exception.
"""


def devisionError():
    try:
        return 5 / 0
    except ZeroDivisionError as err:
        print(err)

devisionError()
