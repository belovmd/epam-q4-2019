"""
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
"""


def read_data(filename):
    try:
        movies = []
        with open(filename, 'r') as file:
            for i in range(28):
                file.readline()

            for i in range(250):
                movie = [i for i in file.readline().strip().split(' ') if i]
                movies.append({
                    "title": ' '.join(movie[3:-1]),
                    "rating": float(movie[2]),
                    "year": int(movie[-1][1:5]),
                })
        return movies
    except IOError:
        print("File not found")


def write_titles(filename, data):
    with open(filename, 'w') as file:
        for movie in data:
            file.write(movie["title"] + '\n')


def create_histogram(data, key):
    histo = {}
    for movie in data:
        histo[movie[key]] = histo.get(movie[key], 0) + 1
    return histo


def write_histogram(filename, histo, symbol='#'):
    keys = sorted(histo.keys())
    with open(filename, 'w') as file:
        for i in range(max(histo.values()), -1, -1):
            for key in keys:
                if histo[key] >= i:
                    file.write(symbol)
                file.write('\t\t')
            file.write('\n')
        for key in keys:
            file.write(str(key) + ' \t')


def main():
    movies = read_data("ratings.list")

    if not movies:
        return

    write_titles("top250_movies.txt", movies)
    histo = create_histogram(movies, "rating")
    write_histogram("ratings.txt", histo)
    histo = create_histogram(movies, "year")
    write_histogram("years.txt", histo)


if __name__ == "__main__":
    main()
