import getpass
import os
import sys


def count_elements_in_list(lst):
    elements_dict = {}
    for el in lst:
        elements_dict[el] = elements_dict.get(el, 0) + 1
    return elements_dict


def create_usual_histogram(lst, filename='histogram.txt', counter=True):
    """compiles horizontal histogram based on a list of data

    if counter = True function will add count of items to the right of the line
    """
    dct = count_elements_in_list(lst)
    max_value = max(dct.values())
    histogram_file = open(filename, "w")

    for key in sorted(dct.keys()):
        histogram_file.write(str(key) + ' |' +
                             '#' * dct[key] +
                             ' ' * (max_value - dct[key]) +
                             '|' + str(dct[key]) * counter +
                             '\n'
                             )
    histogram_file.close()


def create_vertical_histogram(lst, filename='histogram.txt', counter=True):
    """compiles vertical histogram based on a list of data

    if counter = True function will add count of items on top of the column
    """
    dct = count_elements_in_list(lst)
    max_value = max(dct.values())
    max_key_len = max([len(str(x)) for x in dct.keys()])

    histogram_file = open(filename, "w")
    for row in reversed(range(max_value + counter)):
        for key in sorted(dct.keys()):
            if counter and dct[key] == row:  # write count of "#" on column top
                symbol = str(dct[key]).center(max_key_len + 1) * counter
            elif dct[key] > row:
                symbol = '#'
            else:
                symbol = ' '
            histogram_file.write(symbol.center(max_key_len + 1))
        histogram_file.write(' \n')

    for key in sorted(dct.keys()):
        histogram_file.write(key.center(max_key_len) + '|')
    histogram_file.close()


project_directory = os.getcwd()
if getpass.getuser() == 'stych':
    download_directory = r'/home/stych/Downloads'
else:
    download_directory = input('Please input dir with ratings.list file: ')
os.chdir(download_directory)

try:
    ratings_file = open("ratings.list", mode='r', encoding='8859')
except FileNotFoundError:
    print('Не удалось найти файл')
    sys.exit()

data_startline = 28
data_endline = 249
rates_column_num = 2
titles_column_num = 3
years_column_num = -1

head = [next(ratings_file) for x in range(data_startline)]
titles = []
years = []
rates = []
for rows in range(data_endline + 1):
    row_in_data = next(ratings_file)
    split_row = row_in_data.split()
    rates.append(split_row[rates_column_num])
    titles.append(' '.join(split_row[titles_column_num: years_column_num]))
    years.append(split_row[years_column_num].strip('()'))
ratings_file.close()

os.chdir(project_directory)
titles_file = open("top250_movies.txt", "w")
for film_title in titles:
    titles_file.write(film_title + '\n')
titles_file.close()
years = map(lambda year: year[:4], years)
create_vertical_histogram(rates, "ratings.txt")
create_usual_histogram(years, "years.txt")
