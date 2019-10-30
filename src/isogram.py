''' Write program that check str is isogram.'''


def iso(str_):
    str_ = str_.lower()
    dicty = {}
    for sym in str_:
        quantity = str_.count(sym)
        dicty[sym] = quantity
    values = list(dicty.values())
    if len(str_) == values.count(1):
        return True
    else:
        return False


if __name__ == '__main__':
    print(iso('qwet'))
