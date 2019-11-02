"""Recursive finding number palindrome."""


def reverse_number(number, rec_temp=0):
    """Recursive reverse number.

    rec_temp using only for function needs.
    """
    if number == 0:
        return rec_temp
    rec_temp = (rec_temp * 10) + (number % 10)
    return reverse_number(number // 10, rec_temp)


NUMBER = int(input("Enter number: "))
REC_TEMP = reverse_number(NUMBER)

if REC_TEMP == NUMBER:
    print("yes")
else:
    print("no")
