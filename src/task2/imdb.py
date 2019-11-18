from os.path import isfile

# Output filenames
Filename_Top250Titles = 'top250_movies.txt'
Filename_Ratings = 'ratings.txt'
Filename_Years = 'years.txt'

# Field ids in data structure
Id_Name = 0
Id_Rating = 1
Id_Year = 2


def main():
    films_data = read_datafile()

    if not films_data:
        return

    gen_titles(films_data)
    gen_ratings(prepare_ratings(films_data))
    gen_years(prepare_years(films_data))


def gen_ratings(ratings):
    """Generate file with ratings"""

    with open(Filename_Ratings, 'w') as fo:
        for rating, count in ratings.items():
            fo.write("{} {}\n".format(rating, "*" * count))


def prepare_ratings(films_data):
    """Prepare ratings data structure"""

    result = {}

    ratings = [film[Id_Rating] for film in films_data]
    result = {
        film[Id_Rating]: ratings.count(film[Id_Rating])
        for film in films_data
    }

    return result


def gen_years(years):
    """Generate years histogram file"""

    with open(Filename_Years, 'w') as fo:
        for year, count in sorted(years.items()):
            fo.write("{} {}\n".format(year, "*" * count))


def prepare_years(films_data):
    """Prepare years histogram data structure"""

    result = {}

    ratings = [film[Id_Year] for film in films_data]
    result = {
        film[Id_Year]: ratings.count(film[Id_Year])
        for film in films_data
    }

    return result


def gen_titles(films_data):
    """Generate titles file"""

    tiltes = [film[Id_Name] + "\n" for film in films_data]
    with open(Filename_Top250Titles, 'w') as fo:
        fo.writelines(tiltes)


def film_line_to_data(line):
    """Convert text line to output film data structure"""

    items = line.split('  ')
    items[3] = items[3].replace('/I)', ')')

    title = items[3][:-7]
    rating = float(items[2])
    year = int(items[3][-5:-1])

    return (title, rating, year)


def read_datafile():
    """Read input text file"""

    result = []
    data_filename = "ratings.list"
    data_marker = 'New  Distribution  Votes  Rank  Title'

    if not isfile(data_filename):
        print("file not found ", data_filename)
        return

    with open(data_filename, encoding='cp1252') as fo:
        while True:
            line = fo.readline().strip()
            if line == data_marker:
                line = fo.readline().strip()
                while line:
                    result.append(film_line_to_data(line))
                    line = fo.readline().strip()
                else:
                    break
    return result


main()
