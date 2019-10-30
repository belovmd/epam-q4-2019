"""
Given scores of N athletes, find their relative ranks and the people with
the top three highest scores, who will be awarded medals:
"Gold Medal", "Silver Medal" and "Bronze Medal".

N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

example:
input
2 5 4 3 1

output
['4', 'Gold Medal', 'Silver Medal', 'Bronze Medal', '5']
"""


def find_relative_ranks(nums):
    ranks = {}
    sorted_nums = sorted(nums, reverse=True)

    medals = iter(["Gold Medal", "Silver Medal", "Bronze Medal"])
    for score in sorted_nums[:3]:
        ranks[score] = next(medals)

    for relative in sorted_nums[3:]:
        ranks[relative] = str(len(ranks) + 1)

    result = []
    for score in nums:
        result.append(ranks[score])

    return result


nums = [int(i) for i in input().split(' ')]
print(find_relative_ranks(nums))
