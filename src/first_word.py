'''Print first word in string'''


def first_word(str_):
    word = ''
    for sym in str_:
        if sym == ' ':
            break
        else:
            word += sym
    return word


if __name__ == '__main__':
    print(first_word('Hello world'))
