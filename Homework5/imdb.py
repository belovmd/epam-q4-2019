""" On site IMDB you can find different information about movies.
Task is process IMDB ratings data stored in text file and create
histograms. You can find extracted text file in file ./For Homework5/.
Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error
message. Find list of Top250 movies. Extract  titles information.
Create 3 text files top250_movies.txt – contains titles, ratings.txt –
contains histogram for rating, years.txt – contains histogram for years.
Don’t add ratings.list file to PR, but add your created 3 files """

from collections import Counter
import os


def write_titles(file_path):
    titles_path = os.path.join(script_dir, file_path)
    with open(titles_path, 'w') as titles:
        for title in range(len(titles_list)):
            if title != len(titles_list) - 1:
                titles.write(titles_list[title] + '\n')
            else:
                titles.write(titles_list[title])


def write_rating_histogram(file_path):
    ratings_path = os.path.join(script_dir, file_path)
    with open(ratings_path, 'w') as ratings:
        marks_count = Counter(marks_list)
        ascending_marks = sorted(set(marks_list), reverse=True)
        most_met = marks_count.most_common()[0][1]
        for sym_count in range(most_met, 0, -1):
            symbols_in_string = ''
            for mark in ascending_marks:
                if sym_count <= marks_count[mark]:
                    symbols_in_string += '#   '
                else:
                    symbols_in_string += '    '
            ratings.write(symbols_in_string + '\n')
        for mark in ascending_marks:
            ratings.write(mark + ' ')


def write_years_histogram(file_path):
    years_path = os.path.join(script_dir, file_path)
    with open(years_path, 'w') as years:
        years_count = Counter(years_list)
        ascending_years = sorted(set(years_list))
        most_met = years_count.most_common()[0][1]
        for sym_count in range(most_met, 0, -1):
            symbols_in_string = ''
            for year in ascending_years:
                if sym_count <= years_count[year]:
                    symbols_in_string += '# '
                else:
                    symbols_in_string += '  '
            years.write(symbols_in_string + '\n')
        years.write('\n')
        for i in range(4):
            file_string = ''
            for j in range(len(ascending_years)):
                digits_raw = ascending_years[j][i] + ' '
                file_string += digits_raw
            if i != 3:
                years.write(file_string + '\n')
            else:
                years.write(file_string)


script_dir = os.path.dirname(__file__)
top250_path = os.path.join(script_dir, r'For Homework5/ratings.list')
with open(top250_path) as top250:
    titles_list = []
    marks_list = []
    years_list = []
    ind = 0
    while ind < 278:
        data = top250.readline()
        if ind > 27:
            film = ' '.join(data.split()[3:-1])
            mark = data.split()[2]
            year = data.split('(')[1][:4]
            titles_list.append(film)
            marks_list.append(mark)
            years_list.append(year)
        ind += 1

write_titles('top250_movies.txt')
write_rating_histogram('ratings.txt')
write_years_histogram('years.txt')
