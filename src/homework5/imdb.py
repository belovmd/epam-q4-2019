"""
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.
Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
"""


def read_data(filename):
    lines_to_skip = 28
    movies_count = 250

    try:
        movies = []
        with open(filename, 'r', encoding="latin_1") as file:
            for i in range(lines_to_skip):
                file.readline()

            for i in range(movies_count):
                # split line into list where [0] - distribution, [1] - votes,
                # [2] - rating, [3:-1] - title, [-1] - year
                movie = [i for i in file.readline().strip().split(' ') if i]
                movies.append({
                    "title": ' '.join(movie[3:-1]),
                    "rating": float(movie[2]),
                    "year": int(movie[-1][1:5]),  # delete braces in year
                })
        return movies
    except IOError:
        print("File not found")


def write_titles(filename, data):
    with open(filename, 'w', encoding="utf_8") as file:
        for movie in data:
            file.write(movie["title"] + '\n')


def create_histogram(data, key):
    """ return dict where key is name of col and value is height of col """
    histo = {}
    for movie in data:
        histo[movie[key]] = histo.get(movie[key], 0) + 1
    return histo


def write_histogram(filename, histo, symbol='#'):
    keys = sorted(histo.keys())
    width = max([len(str(key)) for key in histo]) + 1
    with open(filename, 'w') as file:
        for i in range(max(histo.values()), 0, -1):
            for key in keys:
                if histo[key] >= i:
                    file.write(symbol.center(width))
                else:
                    file.write(' ' * width)
            file.write('\n')
        for key in keys:
            file.write(str(key).center(width))


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
