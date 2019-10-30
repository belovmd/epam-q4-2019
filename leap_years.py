'''
You are given the year, 
and you have to write a function
to check if the year is leap or not
'''


def LeapYear():
    year = int(input("Enter year: "))

    if year % 4 != 0:
        print("non-leap year")
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("non-leap year")
        else:
            print("leap year")


LeapYear()
