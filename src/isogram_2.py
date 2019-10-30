'''Isogram sedond version'''


def iso(str_):
    if len(str_) == len(set(str_.lower())):
        return True
    else:
        return False


if __name__ == '__main__':
    print(iso('AhaH'))
