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


def read_file(filename):
    try:
        films = []
        i = 0
        with open(filename, "r") as file:
            for line in file:
                if 28 <= i <= 277:
                    words = line.split()
                    films.append({"title": ' '.join(words[3:-1]),
                                 "rating": words[2],
                                  "years": words[-1][1:5]})
                i += 1
        return films
    except IOError:
        print("File not found")


def write_file(filename, data):
    with open(filename, "w") as file:
        for films in data:
            file.write(films["title"] + '\n')


def create_histogram(filename, data, key):
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
