def get_ranges(numbers):
    """Curtails non-empty list of non-repeating integers

    sorted in ascending order
    """
    curtail_numbers = ''
    index = 0
    while index < len(numbers) - 1:
        if numbers[index] + 1 != numbers[index + 1]:
            curtail_numbers += str(numbers[index]) + ','
        elif numbers[index] - 1 != numbers[index - 1]:
            curtail_numbers += str(numbers[index]) + '-'
        index += 1
    curtail_numbers += str(numbers[-1])
    return curtail_numbers


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
