"""
On site IMDB you can find different information about movies.
Task is process IMDB ratings data stored in text file and
create histograms. You can find extracted text file in file
./For Homework5/.
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with
error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles,
ratings.txt – contains histogram for rating, years.txt –
contains histogram for years.
Don’t add ratings.list file to PR, but add your created 3 files
"""
START_OF_FILE = 28
END_OF_FILE = 277
TIT_POS = 3
END_TITLE = -1
RATING_POS = 2
YEAR_POS = -1
ST_YEAR = 1
END_YEAR = 5


def read_file(filename):
    try:
        films = []
        i = 0
        with open(filename, "r") as file:
            for line in file:
                if START_OF_FILE <= i <= END_OF_FILE:
                    words = line.split()
                    films.append({"title": ' '.join(words[TIT_POS:END_TITLE]),
                                 "rating": words[RATING_POS],
                                  "years": words[YEAR_POS][ST_YEAR:END_YEAR]})
                i += 1
        return films
    except IOError:
        print("File not found")


def write_file(filename, data):
    with open(filename, "w") as file:
        for films in data:
            file.write(films["title"] + '\n')


def create_histogram(filename, data, key):
    """Create Histogram

    :param filename: file name
    :type filename: string
    :param data: list of movie dictionary storage
    :type data: list
    :param key: dictionary key
    :type key: string
    :return: dict
    """
    histogram = {}
    for films in data:
        histogram[films[key]] = histogram.get(films[key], 0) + 1
    new_key = sorted(histogram.keys())
    with open(filename, "w") as file:
        for films in new_key:
            file.write(films + ' ' + histogram[films] * '#' + '\n')


def main():
    films = read_file('ratings.list')
    if films:
        write_file('top250_films.txt', films)
        create_histogram('rating.txt', films, 'rating')
        create_histogram('years.txt', films, 'years')


if __name__ == '__main__':
    main()
