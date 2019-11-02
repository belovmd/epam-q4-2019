"""Each of the n cards has numbers written on the both sides of it.
The first card has 0 and 1 on it, the second has 1 and 2, …,
the n-th has (n−1) and n. First-grade pupil Nick takes cards one by one
in random order and reads the number on one of the sides. Nick is not
very good with numbers, so it is possible that he makes a mistake.
Your task is to find out if he was mistaken, i.e. if the given sequence
of numbers is possible for some order of taking cards.
Input
The first line contains numbers n, the total number of cards, and m,
the number of the cards that were taken. Starting with the second line,
the m non-negative integers are listed (the sequence read by Nick).
One or more spaces or line feeds separate the numbers.
1 ≤ n ≤ 1000
Output
Write YES if the given sequence of numbers is possible
for some order of taking cards, NO otherwise."""
import sys

n, m = [int(x) for x in input().split()]
cards = [0] * n
numbers = [int(x) for x in sys.stdin.read().split()]
for number in numbers:
    if 0 < number < n:
        cards[number - 1] = cards[number] = 1
    elif not number:
        cards[number] = 1
    else:
        cards[number - 1] = 1
print("YES" if sum(cards) >= m else "NO")
