"""Application "imdb.py" can open and read "ratings.list" file.

If rating.list file does not exists, script completes with error message.
Application finds list of Top250 movies and:
extracts titles information to "top250_movies.txt";
creates histogram for rating in "ratings.txt";
creates histogram for years in "years.txt".
"""
import os

path = input('Please input full path to "ratings.list" file:')
if path[-1] == '\\':
    file_path = os.path.join(path, "ratings.list")
else:
    file_path = os.path.join(path, "\\ratings.list")
try:
    with open(file_path) as ratings_list:
        top250 = open('top20_movies.txt', 'w')
        rating_histogram = open('rating.txt', 'w')
        years_histogram = open('years.txt', 'w')
        rating = []
        years = []
        for num, line in enumerate(ratings_list):
            if num in range(28, 278):
                top250.write(' '.join(line.split()[3:-1]) + '\n')
                rating.append(line.split()[2])
                years.append(line.split()[-1][1:-1])
        top250.close()
        for rate in sorted(set(rating), reverse=True):
            rating_histogram.write(rate + ' ' +
                                   '#' * rating.count(rate) + '\n')
        rating_histogram.close()
        for year in sorted(set(years), reverse=True):
            years_histogram.write(year + ' ' +
                                  '#' * years.count(year) + '\n')
        years_histogram.close()
except FileNotFoundError:
    print("File \"ratings.list\" doesn\'t exist")
