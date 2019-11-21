"""Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
"""

from collections import OrderedDict
import os


try:
    film_list = []
    with open(os.path.join(
            'c:' + os.sep, 'Homework5', 'ratings.list'), 'r') as file:
        for i in range(28):
            file.readline()

        for index in range(250):
            movie = [index for index in file.readline().strip().split(
                ' ') if index]
            print(movie)
            film_list.append({
                "title": ' '.join(movie[3:-1]),
                "rate": float(movie[2]),
                "year": int(movie[-1][1:5]),
            })
except IOError:
    print("File not found")

try:
    with open(os.path.join(
            'c:' + os.sep, 'Homework5', 'top250_movies.txt'), 'w') as file:
        index = 0
        for film in film_list:
            index += 1
            file.write(str(index) + '. ' + film["title"] + '\n')
except IOError:
    print("File not found")


dict_years = {}
for film in film_list:
    if film["year"] in dict_years:
        dict_years[film["year"]] += 1
    else:
        dict_years[film["year"]] = 1

sortedDict = OrderedDict(sorted(dict_years.items()))
try:
    with open(os.path.join(
            'c:' + os.sep, 'Homework5', 'years.txt'), 'w') as file:
        for key in sortedDict.keys():
            file.write(str(key) + '  ')
            for i in range(sortedDict[key]):
                file.write('*')
            file.write('   ' + str(sortedDict[key]))
            file.write('\n')
except IOError:
    print("File not found")

dict_ratings = {}
for film in film_list:
    if film["rate"] in dict_ratings:
        dict_ratings[film["rate"]] += 1
    else:
        dict_ratings[film["rate"]] = 1

sortedDict = OrderedDict(sorted(dict_ratings.items()))
try:
    with open(os.path.join(
            'c:' + os.sep, 'Homework5', 'ratings.txt'), 'w') as file:
        for key in sortedDict.keys():
            file.write(str(key) + '  ')
            for i in range(sortedDict[key]):
                file.write('*')
            file.write('   ' + str(sortedDict[key]))
            file.write('\n')
except IOError:
    print("File not found")
