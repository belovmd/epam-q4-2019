"""Task from checkio - 'Pawn Brotherhood'
You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.
"""


def safe_pawns(pawns: set):
    w = " abcdefgh "
    ans = 0
    for item in pawns:
        if (w[w.find(item[0]) - 1] + (str(int(item[1]) - 1)) in pawns) or \
             ((w[w.find(item[0]) + 1] + (str(int(item[1]) - 1))) in pawns):
            ans += 1

    return ans


print("Example")
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
