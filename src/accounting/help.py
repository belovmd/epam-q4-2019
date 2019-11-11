import json as js
from os import listdir, getcwd


def create_outfile():
    path = getcwd()
    cwd_files = listdir(path)
    if 'data.json' not in cwd_files:
        with open('data.json', 'w') as wr_file:
            js.dump({}, wr_file)


def rd_dict():
    try:
        with open('data.json', 'r') as rd_file:
            dict_ = js.load(rd_file)
    except Exception as ex:
        return ex
    else:
        return dict_


def show_all(dict_):
    str_ = ''
    for key_value in dict_.items():
        str_ += ':'.join(key_value) + '\n'
    return str_


if __name__ == '__main__':
    create_outfile()
    print(rd_dict())
