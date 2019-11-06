"""Task from checkio 'Xs and Os Referee' (Check, who won)"""

from typing import List


def checkio(game_result: List[str]) -> str:
    if (game_result[0].count("X") == 3) or \
            (game_result[1].count("X") == 3) or \
            (game_result[2].count("X") == 3):
        return "X"
    if (game_result[0].count("O") == 3) or \
            (game_result[1].count("O") == 3) or \
            (game_result[2].count("O") == 3):
        return "O"
    if game_result[0][0] == game_result[1][0] == game_result[2][0] != ".":
        return game_result[0][0]
    if game_result[0][1] == game_result[1][1] == game_result[2][1] != ".":
        return game_result[0][1]
    if game_result[0][2] == game_result[1][2] == game_result[2][2] != ".":
        return game_result[0][2]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != ".":
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] != ".":
        return game_result[2][0]

    return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))
