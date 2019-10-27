"""You are given three integers representing the dimensions of a cuboid along
with an integer n. You have to print a list of all possible coordinates on a
3D grid where the sum is not equal to n.

Input Format
Four integers each on four separate lines, respectively.

Constraints
Print the list in lexicographic increasing order."""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in
           range(z + 1) if (i + j + k != n)])
