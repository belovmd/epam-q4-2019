""" Find list of top250 movies in ratings.list. Create 3 text file:
  top250_movies - contains titles, rating - contains histogram for rating,
   years - contains histogram for years """
from collections import Counter
from collections import defaultdict


def rd_data():
    data = defaultdict(list)
    try:
        with open('ratings.list', 'r') as rd_file:
            for num, line in enumerate(rd_file):
                if num in range(0, 278):
                    if num in range(28, 278):
                        list_line = line.split()
                        data['title'].append(' '.join(list_line[3:-1]))
                        data['rank'].append(list_line[2])
                        data['year'].append(list_line[-1][1:-1])
                else:
                    break
    except FileNotFoundError as exc:
        return exc
    return data


def wr_title(data, file, key='title'):
    if key == 'title':
        with open(file + '.txt', 'w') as wr_file:
            wr_file.write('\n'.join(data[key]))
        return 'Done'
    else:
        return 'You should use other func '


def wr_other(data, key_, file):
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


def wr_other2(data, key, file, space=3, sym='x'):
    data = dict(Counter(data[key]))
    max_len_key = len(max(data.keys()))
    out_str = ''
    for key in sorted(data.keys()):
        len_key = len(key)
        difference = max_len_key - len_key
        indent = difference * ' '
        quantity_sym = data[key]
        data[key] = indent + data[key] * (sym + ' ' * space)
        out_str += '{0}{1}:{2} \n'.format(key, data[key], quantity_sym)
    with open(file + '.txt', 'w') as wr_file:
        wr_file.write(out_str)
    return out_str


if __name__ == '__main__':
    data = rd_data()
    # print(wr_title(data, 'top250_movies'))
    # print(wr_other(data, 'rank', 'ranting'))
    # print(wr_other(data, 'year', 'years'))
    print(wr_other2(data, 'rank', 'ranting2'))
    print(wr_other2(data, 'year', 'years2'))
