"""
Task from Codewars.
Change all letters, except last 4, to "#"
"""


def maskify(cc):
    return "#"*(len(cc) - 4) + cc[-4:]


cc = input()

if len(cc) < 5:
    print(cc)
else:
    print(maskify(cc))
