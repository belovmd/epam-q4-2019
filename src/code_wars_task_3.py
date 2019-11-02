"""Define open or senior clubber.

The Western Suburbs Croquet Club has two categories of membership,
Senior and Open. They would like your help with an application form
that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a
handicap greater than 7. In this croquet club, handicaps range from -2
to +26; the better the player the lower the handicap.
"""


def openOrSenior(data):
    """Return array open or senior."""
    return ["Senior" * (piece_data[0] >= 55 and piece_data[1] > 7) or "Open"
            for piece_data in data]
