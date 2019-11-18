"""On site IMDB you can find different information about movies. Task is
process IMDB ratings data stored in text file and create histograms. You can
find extracted text file in file ./For Homework5/.
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
Don’t add ratings.list file to PR, but add your created 3 files"""

import re


def list_to_dict(lst):
    dct = {elem: lst.count(elem) for elem in lst}
    return dct


def histogram(dct, file_name):
    maximal = max(dct.values())
    # we need length of key to format histogram correctly
    key_len = len(max(dct.keys()))

    with open(file_name, "w") as file_to_write:
        while maximal > 0:
            for value in dct.values():
                if value >= maximal:
                    file_to_write.write("#" + " " * key_len)
                else:
                    file_to_write.write(" " + " " * key_len)
            file_to_write.write("\n")
            maximal -= 1
        for key in dct.keys():
            file_to_write.write(str(key) + " " * key_len)


year_lst = []
rating_lst = []
file = open("ratings.list")
top = open("top250_movies.txt", "w")
file.readline(27)

for position, line in enumerate(file):
    if position > 277:
        break
    if position > 27:
        # split by 2 or more whitespaces
        movie = re.split(r" {2,}", line.strip())
        rating_lst.append(movie[2])

        # split title and year ([0] - title, [1] - year)
        movie = movie[-1].split(" (")
        title = movie[0]
        top.write(title + "\n")

        # magic number 4 is the number of digits in the year number
        year_lst.append(movie[1][:4])

file.close()
top.close()

histogram(list_to_dict(sorted(rating_lst)), "ratings.txt")
histogram(list_to_dict(sorted(year_lst)), "years.txt")
