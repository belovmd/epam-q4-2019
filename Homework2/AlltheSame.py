"""
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.
"""
from typing import List
from typing import Any


def all_the_same(elements: List[Any]) -> bool:
    return len(set(elements)) <= 1


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
