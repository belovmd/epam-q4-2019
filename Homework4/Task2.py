def get_ranges(nums):
    """Curtails non-empty list of non-repeating integers

    sorted in ascending order
    """
    curtail_nums = ''
    ind = 0
    while ind < len(nums) - 1:
        current_num = nums[ind]
        next_num = nums[ind + 1]
        prev_num = nums[ind - 1]
        if current_num + 1 != next_num:
            comma = str(current_num) + ','
            curtail_nums += comma
        elif current_num - 1 != prev_num:
            dash = str(current_num) + '-'
            curtail_nums += dash
        ind += 1
    curtail_nums += str(nums[-1])
    return curtail_nums


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
