#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8

"""
EPAM python q4 homework 05 2
Sergey Streltsov 2019-11-17
"""

import os
import sys
from operator import itemgetter


def load_ratings(filename):
    run_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(run_path, filename)
    if os.path.isfile(full_path):
        top250 = list()
        is_top250 = False
        is_header = False
        with open(full_path, 'r', encoding='cp1252') as in_file:
            for idx, line in enumerate(in_file):
                if 'TOP 250 MOVIES' in line:
                    is_top250 = True
                    continue
                if is_top250 and ('Votes  Rank  Title' in line):
                    is_header = True
                    count = 0
                    continue
                if is_top250 and is_header:
                    top250.append(line)
                    count += 1
                    if count == 250:
                        break
    else:
        sys.exit('Error: No file {} found'.format(full_path))
    return top250, run_path


if __name__ == '__main__':
    ratings, f_path = load_ratings('ratings.list')
    ratio_db = dict()
    year_db = dict()
    out_path = os.path.join(f_path, 'top250_movies.txt')
    with open(out_path, 'w', encoding='cp1252') as out_file:
        for item in ratings:
            splitted_str = item.split()
            title = ' '.join(splitted_str[3:-1])
            ratio = splitted_str[2]
            ratio_db[ratio] = ratio_db.get(ratio, 0) + 1
            year = splitted_str[-1][1:-1]
            year_db[year] = year_db.get(year, 0) + 1
            # print(title, ratio, year)
            out_file.write(title + '\n')
    out_path = os.path.join(f_path, 'ratings.txt')
    with open(out_path, 'w', encoding='cp1252') as out_file:
        for key, value in sorted(ratio_db.items(), key=itemgetter(1),
                                 reverse=True):
            out_file.write(key + ': ' + '#' * value + '\n')
    out_path = os.path.join(f_path, 'years.txt')
    with open(out_path, 'w', encoding='cp1252') as out_file:
        for key, value in sorted(year_db.items(), key=itemgetter(1),
                                 reverse=True):
            out_file.write(key + ': ' + '#' * value + '\n')

