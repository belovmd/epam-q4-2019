"""On site IMDB you can find different information about movies. Task is
process IMDB ratings data stored in text file and create histograms. You can
find extracted text file in file ./For Homework5/.
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
Don’t add ratings.list file to PR, but add your created 3 files"""
from collections import Counter
import os


def count_and_write_to_file(filename, column):
    data = Counter([movie[column] for movie in movies_top250])
    min_value, max_value = min(data.values()), max(data.values())
    max_len = len(str(max_value))
    max_key_len = max(len(str(key)) for key in data) + 1
    data_order = sorted(data)
    filepath = os.path.join("homework5", "2", "data", filename)
    with open(filepath, "w") as file:
        for value in range(max_value, min_value - 1, -1):
            file.write(str(value).rjust(max_len))
            [file.write("#".rjust(max_key_len) if data[key] >= value
                        else " ".rjust(max_key_len)) for key in data_order]
            file.write("\n")
        file.write((max_len + 1) * " ")
        [file.write(str(key).rjust(max_key_len)) for key in data_order]


movies_top250 = []
try:
    path = os.path.join("homework5", "2", "data", "ratings.list")
    with open(path, encoding="latin_1") as rating_file:
        for i, line in enumerate(rating_file):
            if i == 27:  # read keys
                keys = line.split()
                keys.append("Year")
            elif 27 < i <= 277:  # read movies
                movie = [""] + line.strip().split(None, 3)
                movie = movie[:-1] + movie[-1].rsplit(" ", 1)  # separate year
                movie[-1] = movie[-1][1:5]  # delete braces
                movies_top250.append(dict(zip(keys, movie)))
            elif i > 277:  # 27+250
                break

        t_path = os.path.join("homework5", "2", "data", "top250_movies.txt")
        with open(t_path, "w", encoding="utf_8") as titles_file:
            [titles_file.write(movie["Title"] + "\n") for movie in
             movies_top250]

        count_and_write_to_file("ratings.txt", "Rank")

        count_and_write_to_file("years.txt", "Year")
except Exception as e:
    print(str(e))
