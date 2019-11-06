"""The new "Avengers" movie has just been released!
There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
Vasya is currently working as a clerk.
He wants to sell a ticket to every single person in this line.
Can Vasya sell a ticket to every person and give change
if he initially has no money and sells the tickets strictly in the order people queue?
Return YES, if Vasya can sell a ticket to every person and
give change with the bills he has at hand at that moment. Otherwise return NO.
"""


def tickets(people):
    count25, count50 = 0, 0
    for i in people:
        if i == 25:
            count25 += 1
        if i == 50:
            count25 -= 1
            count50 += 1
        if i == 100:
            if count50 == 0:
                count25 -= 3
            else:
                count25 -= 1
                count50 -= 1
        if count25 < 0:
            return "NO"
    return "YES"
