def is_palindrome(number=12321):
    """Determine if given number is palindrome."""

    buff = number
    reversed = 0

    while buff:
        reversed *= 10
        reversed += buff % 10
        buff //= 10

    result = reversed == number
    # print("is {} palindrome?: {}".format(number, result))
    return result


def generate_numbers(num=20):
    """Generate_numbers

    Define a function generate_numbers(number) which returns a dictionary
    where the keys are numbers between 1 and n (both included)
    and the values are square of keys. n – function argument.
    Default is 20."""
    result = {el: el**2 for el in range(1, num + 1)}

    return result
    # print(result)


print(generate_numbers(5))
