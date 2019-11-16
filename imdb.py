import os
import getpass
import sys


def count_elements_in_list(lst):
    elements_dict = {}
    for el in lst:
        elements_dict[el] = elements_dict.get(el, 0) + 1
    return elements_dict


def nice_hat_for_years_file(years_file, counter=True):
    years_file.write('Year | Amount  |' + counter * 'A' + '\n')
    years_file.write('_____|_________|' + counter * '_' + '\n')


def create_histogram(lst, filename='histogram.txt', vertical=True,
                     vertical_style=2, counter=True, years_hat=False):
    dct = count_elements_in_list(lst)
    max_value = max(dct.values())
    max_key_len = max([len(str(x)) for x in dct.keys()])
    matrix = []
    keys_list = []

    histogram_file = open(filename, "w")

    if not vertical:
        if years_hat:
            nice_hat_for_years_file(histogram_file, counter)
        for key in sorted(dct.keys()):
            matrix.append(str(key) + ' |' +
                          '#' * dct[key] +
                          ' ' * (max_value - dct[key]) +
                          '|' + str(dct[key]) * counter)
        for row1 in matrix:
            histogram_file.write(row1 + '\n')
    else:
        for key in sorted(dct.keys()):
            matrix.append(' ' * (max_value - dct[key]) + '#' * dct[key])
            keys_list.append(str(key) + ' ' * (max_key_len - len(str(key))))
            ziped = zip(*matrix)

        if vertical_style == 1:
            for row in ziped:
                for symb in row:
                    histogram_file.write(symb + ' ')
                histogram_file.write(' \n')

            for row in zip(*keys_list):
                for symb in row:
                    histogram_file.write(symb + '|')
                histogram_file.write('\n')
        else:
            for row in ziped:
                histogram_file.write(' ' * (max_key_len // 2))
                for symb in row:
                    histogram_file.write(symb + ' ' * max_key_len)
                histogram_file.write('\n')
            for row in keys_list:
                histogram_file.write(row + '|')
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


head = [next(ratings_file) for x in range(28)]
titles = []
years = []
rates = []
for rows in range(250):
    row = next(ratings_file)
    rates.append(row.split()[2])
    titles.append(' '.join(row.split()[3:]))
    years.append(row.split()[-1].strip('()'))
ratings_file.close()

os.chdir(project_directory)
titles_file = open("top250_movies.txt", "w")
for film_title in titles:
    titles_file.write(film_title + '\n')
titles_file.close()

years = map(lambda year: year[:4], years)
create_histogram(rates, "ratings.txt", vertical=True, vertical_style=2)
create_histogram(years, "years.txt", vertical=False,
                 counter=True, years_hat=True)
