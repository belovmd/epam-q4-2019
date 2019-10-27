"""You are given a set  and  other sets.
Your job is to find whether set is a strict superset of the sets.
A strict superset has at least one element that does not exist in its subset.

Input Format
The first line contains the space separated elements of set.
The second line contains the number of other sets.
The next lines contains the space separated elements of the other sets.

Output Format
Print True if set  is a strict superset of all other  sets. Otherwise,
print False."""
a = set([int(x) for x in input().split()])
n = int(input())
while n:
    t = set([int(x) for x in input().split()])
    if not a.issuperset(t):
        print(False)
        break
    n -= 1
else:
    print(True)
