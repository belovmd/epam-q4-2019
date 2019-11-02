"""Input
The input stream contains a set of integer numbers.
The numbers are separated by any number of spaces and line breaks.
A size of the input stream does not exceed 256 KB.
Output
For each number from the last one till the first one you should output its
square root. Each square root should be printed in a separate line
with at least four digits after decimal point."""
from math import sqrt
import sys

input_data = reversed(sys.stdin.read().split())
[print(sqrt(float(num))) for num in input_data]
