""" Функции для создания словаря, считывания, 
сохарнения и преобразования в строку
create_outfile - вызывается при запуске программы,
создает файл data.json, который хранит пустой словарь
rd_dict - считывает файл data.json, вызывается при каждом запуске программы
save_dict - перезаписывает файл data.json, вызывается принажатии на кнопку save
show_all - преобразовывает словарь в строку,
вызывается при нажатии на кнопку show_all"""

import json as js
from os import getcwd
from os import listdir


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


def save_dict(dict_):
    with open('data.json', 'w') as wr_file:
        js.dump(dict_, wr_file, indent=2)


def show_all(dict_):
    str_ = ''
    for key_value in dict_.items():
        str_ += ':'.join(key_value) + '\n'
    return str_


if __name__ == '__main__':
    create_outfile()
    print(rd_dict())
