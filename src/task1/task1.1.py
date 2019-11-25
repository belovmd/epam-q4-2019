def danger_call():
    """Handle Zero Division exception."""

    try:
        return 5 / 0
    except ZeroDivisionError as e:
        print("got exeption:", e)
    else:
        print("no exception")


danger_call()
