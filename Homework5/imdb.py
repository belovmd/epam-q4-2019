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
        symbols_in_marks = []
        for mark in marks_list:
            symbols = int(mark.split(',')[0]) * 10 + int(mark.split(',')[1])
            symbols_in_marks.append(symbols)
        marks_count = Counter(symbols_in_marks)
        symbols_in_string = 0
        for symb_count in range(max(symbols_in_marks), 0, -1):
            symbols_in_string += marks_count[symb_count]
            ratings.write('#   ' * symbols_in_string + '\n')
        for mark in marks_list:
            ratings.write(mark + ' ')


def write_years_histogram(file_path):
    years_path = os.path.join(script_dir, file_path)
    with open(years_path, 'w') as years:
        yr_count = Counter(years_list)
        count_yr = {}
        for yr in yr_count:
            count_yr[yr_count[yr]] = count_yr.get(yr_count[yr], []) + [yr]
        count_exist = sorted(count_yr, reverse=True)
        ascending_years = sorted(set(years_list))
        for count in range(len(count_exist) - 1):
            file_string = ''
            for year in ascending_years:
                if year not in count_yr[count_exist[count]]:
                    file_string += '  '
                else:
                    file_string += '# '
                    count_yr[count_exist[count + 1]] += [year]
            years.write(file_string + '\n')
        years.write('# ' * len(ascending_years) + '\n\n')
        ascending_years_str = [str(i) for i in ascending_years]
        for i in range(3, -1, -1):
            file_string = ''
            for j in range(len(ascending_years_str)):
                file_string += ascending_years_str[j][i] + ' '
            if i:
                years.write(file_string + '\n')
            else:
                years.write(file_string)


script_dir = os.path.dirname(__file__)
top250_path = os.path.join(script_dir, r'For Homework5/rating.list')
with open(top250_path) as top250:
    titles_list = []
    marks_list = []
    years_list = []
    data = top250.readline()
    while data:
        titles_list.append(data.split('(')[0][5:-1])
        marks_list.append(data.split()[-1])
        years_list.append(int(data.split('(')[1][:4]))
        data = top250.readline()

write_titles('top250_movies.txt')
write_rating_histogram('ratings.txt')
write_years_histogram('years.txt')
