"""Task from checkio 'Xs and Os Referee' (Check, who won)
Changed:
Now size of the matrix and number of Xs and Os to win are
mutable.
"""


# Checks if there is a winner
def check_winner(lst, wn):
    num = 1
    prev_symbol = lst[0]
    lst += "."
    for symbol in lst[1:]:
        if symbol == prev_symbol:
            num += 1
            prev_symbol = symbol
        else:
            if num >= wn and prev_symbol != ".":
                return prev_symbol
            prev_symbol = symbol
            num = 1


# Line check
def check_line(game_field, wn):
    n = len(game_field[0])
    for i in range(n):
        ans = check_winner(game_field[i], wn)
        if ans:
            return ans


# Column check
def check_column(game_field, wn):
    n = len(game_field[0])
    new_lst = ["."] * n
    for i in range(n - wn + 1):
        for j in range(n):
            new_lst[j] = game_field[j][i]

        return check_winner(new_lst, wn)


# Diagonal(left to right) check
def check_diagonal_lr(game_field, wn):
    n = len(game_field[0])
    new_lst1 = ["."] * n
    new_lst2 = ["."] * n

    for i in range(n - wn + 1):
        for j in range(n - i):
            new_lst1[j] = game_field[j][i + j]
            new_lst2[j] = game_field[i + j][j]
        ans = check_winner(new_lst1, wn)
        if ans:
            return ans
        ans = check_winner(new_lst2, wn)
        if ans:
            return ans


# Diagonal(right to left check)
def check_diagonal_rl(game_field, wn):
    n = len(game_field[0])
    new_lst1 = ["."] * n
    new_lst2 = ["."] * n
    for i in range(n - wn + 1):
        for j in range(n - i):
            new_lst1[j] = game_field[j][n - i - j - 1]
            new_lst2[j] = game_field[i + j][n - i - j - 1]

        ans = check_winner(new_lst1, wn)
        if ans:
            return ans
        ans = check_winner(new_lst2, wn)
        if ans:
            return ans


def xo_referee(game_field, wn):

    ans = check_line(game_field, wn)

    if ans:
        return ans
    ans = check_column(game_field, wn)
    if ans:
        return ans
    ans = check_diagonal_lr(game_field, wn)
    if ans:
        return ans
    ans = check_diagonal_rl(game_field, wn)
    if ans:
        return ans

    return "D"


if __name__ == '__main__':
    print("Example:")
    win_number = int(input("Enter win number"))
    print(xo_referee(["XOXXOOO",
                      "X......",
                      ".X..O..",
                      "..XO...",
                      "..OXXX.",
                      ".O..O..",
                      "O......"], win_number))

#    X......
#    .X.....
#    ..X....
#    ...X...
#    ....X..
#    .......
#    .......
