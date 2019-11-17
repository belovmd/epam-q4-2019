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
films = []
rating = []
years = []
try:
    with open(file_path) as ratings_list:
        for num, line in enumerate(ratings_list):
            if num in range(28, 278):
                film_name_start = 3
                film_name_end = -1
                films.append(' '.join(line.split()[film_name_start:
                                                   film_name_end]))
                rating_column = 2
                rating.append(line.split()[rating_column])
                years_column = -1
                year_start_pos = 1
                year_end_pos = 5
                years.append(line.split()[years_column][year_start_pos:
                                                        year_end_pos])
except FileNotFoundError:
    print("File \"ratings.list\" doesn\'t exist")

with open('top20_movies.txt', 'w') as top250:
    for film in films:
        top250.write(film + '\n')
with open('rating.txt', 'w') as rating_histogram:
    for rate in sorted(set(rating), reverse=True):
        rating_histogram.write(rate + ' ' + '#' * rating.count(rate) + '\n')
with open('years.txt', 'w') as years_histogram:
    for year in sorted(set(years), reverse=True):
        years_histogram.write(year + ' ' + '#' * years.count(year) + '\n')
