"""Write a function to compute 5/0 and use try/except to catch the
DevisionError exception."""
try:
    result = 5 / 0
except ZeroDivisionError as error:
    print("Something bad occurred: " + str(error))
