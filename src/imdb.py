""" Find list of top250 movies in ratings.list. Create 3 text file:
  top250_movies - contains titles, rating - contains histogram for rating,
   years - contains histogram for years """
from collections import Counter
from collections import defaultdict


def read_data():
    data = defaultdict(list)

    start_line = 28
    end_line = 278

    index_rank = 2
    index_year = -1

    start_year = 1
    end_year = 5
    start_title = 3

    try:
        with open('ratings.list', 'r') as rd_file:
            for num, line in enumerate(rd_file):
                if num in range(end_line):
                    if num in range(start_line, end_line):
                        list_line = line.split()
                        data['title'].append(
                            ' '.join(list_line[start_title:index_year]))
                        data['rank'].append(list_line[index_rank])
                        data['year'].append(
                            list_line[index_year][start_year:end_year])
                else:
                    break
    except FileNotFoundError as exc:
        return exc
    return data


def write_title(data, file):
    with open(file + '.txt', 'w') as wr_file:
        wr_file.write('\n'.join(data['title']))
    return 'Done'


"""Keys: year, rank """


def write_other(data, key_, file):
    data = dict(Counter(data[key_]))  # key -x, value -y
    height = max(data.values())
    lst_str = [[str(line)] for line in range(height, 0, -1)]  # elem - str
    for key in sorted(data.keys()):
        len_str = len(key)
        for lst in range(len(lst_str)):
            indent = len(lst_str[lst][0]) - 1
            space_x = len_str // 2
            space_after_x = space_x - 1 + len_str % 2 + indent
            space_x -= indent
            if len(lst_str) - data[key] <= lst:
                lst_str[lst].append(' ' * space_x + 'x' + ' ' * space_after_x)
            else:
                lst_str[lst].append(' ' * len_str)
    lst_str.append(sorted(data.keys()))
    lst_str[-1].insert(0, ' ')
    first_str = 'x - {0} y - quantity of films'.format(key_)
    lst_str.insert(0, first_str)
    out_str = ''
    for line in lst_str:
        out_str += ' '.join(line) + '\n'
    with open(file + '.txt', 'w') as wr_file:
        wr_file.write(out_str)

    return out_str


"""Second version for write histogram. keys: rank,year.
Space - space between columns"""


def write_other2(data, key, file, space):
    data = dict(Counter(data[key]))
    max_len_key = len(max(data.keys()))
    out_str = ''
    for key in sorted(data.keys()):
        len_key = len(key)
        difference = max_len_key - len_key
        indent = difference * ' '
        quantity_sym = data[key]
        data[key] = indent + data[key] * ('x' + ' ' * space)
        out_str += '{0}{1}:{2} \n'.format(key, data[key], quantity_sym)
    with open(file + '.txt', 'w') as wr_file:
        wr_file.write(out_str)
    return out_str


if __name__ == '__main__':
    data = read_data()
    print(write_title(data, 'top250_movies'))
    print(write_other(data, 'rank', 'ranting'))
    print(write_other(data, 'year', 'years'))
    print(write_other2(data, 'rank', 'ranting2', 3))
    print(write_other2(data, 'year', 'years2', 3))
