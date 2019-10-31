"""You are given an integer, n. Your task is to print an alphabet rangoli of
size n. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:

#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a,
and the boundary has the n-th alphabet letter (in alphabetical order).

Input Format
Only one line of input containing n, the size of the rangoli.

Output Format
Print the alphabet rangoli in the format explained above."""
from string import ascii_lowercase as alphabet

size = int(input())
for i in range(1, size * 2):
    for j in range(1, size * 4 - 2):
        distance = abs(size - i) + abs(size * 2 - 1 - j) // 2
        print(alphabet[distance] if j % 2 and distance < size else "-",
              end="")
    print()
