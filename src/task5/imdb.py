"""
Task is process IMDB ratings data stored in text file and create histograms.

Our application imdb.py can open and read ratings.list file.
If rating.list file does not exists, script completes with error message.

Create 3 text files
top250_movies.txt – contains titles,
ratings.txt – contains histogram for rating,
years.txt – contains histogram for years.

Don’t add ratings.list file to PR, but add your created 3 files
"""


import re


def extract_top250_table():
    """Takes TOP250 table from ratings list as string"""
    file_path = "ratings.list"
    re_head = re.compile(r'^New {2}Distribution {2}Votes {2}Rank {2}Title$')
    re_killswitch = re.compile(r'BOTTOM 10 MOVIES')
    extracted_tbl = ''

    with open(file_path, "r", encoding="ISO-8859-1") as f_obj:
        start, end, killswitch = False, False, False
        for line in f_obj:
            if re_killswitch.search(line):
                killswitch = True
                break
            if re_head.search(line):
                start = True
                end = False
            elif line.isspace():
                end = True
            if start and not end and not killswitch:
                extracted_tbl += line
                if end or killswitch:
                    break
    return extracted_tbl


def create_file(filename='newfile.txt', my_data=extract_top250_table()):
    my_file = open(filename, 'w')
    my_file.write(my_data)
    my_file.close()


def extract_titles_to_file(out_filename='top_250_files.txt',
                           data_filename='newfile.txt'):
    with open(data_filename, "r", encoding="ISO-8859-1") as f_obj:
        # skip header
        f_obj.readline().split()
        splitter = re.compile(r'\s{2,}')
        with open(out_filename, "w", encoding="ISO-8859-1") as inner_f_obj:
            for line in f_obj:
                title = re.split(splitter, f_obj.readline())[4]
                inner_f_obj.write(title)


def create_rating_dictionary(data_filename='newfile.txt'):
    with open(data_filename, "r", encoding="ISO-8859-1") as f_obj:
        # skip header
        splitter = re.compile(r"\s{2,}")
        histogram_dict = {}
        for line in f_obj:
            title = (re.split(splitter, line)[4])[:-1]
            rating = re.split(splitter, line)[3]
            histogram_dict[title] = rating
    return histogram_dict


def create_years_dictionary(data_filename='newfile.txt'):
    with open(data_filename, "r", encoding="ISO-8859-1") as f_obj:
        # skip header
        f_obj.readline().split()
        splitter = re.compile(r'\s{2,}')
        years_extractor = re.compile('\\(\\d{4}\\)')
        histogram_dict = {}
        for line in f_obj:
            title = (re.split(splitter, line)[4])[:-1]
            if re.search(years_extractor, line):
                year = re.findall(years_extractor, line)[0]
                histogram_dict[title] = year[1:-1]
    return histogram_dict


def historam_of_dictionary_values(histogram_dict):
    result = ''
    counter = {}
    for key, value in histogram_dict.items():
        if value in counter:
            counter[value] += 1
        else:
            counter[value] = 1
    for key, value in counter.items():
        result += '{}: {}\n'.format(key, value * '#')
    return result


if __name__ == "__main__":

    extract_top250_table()
    create_file()
    extract_titles_to_file()
    create_file(filename='ratings.txt', my_data=historam_of_dictionary_values(
        create_rating_dictionary()))
    create_file(filename='years.txt', my_data=historam_of_dictionary_values(
        create_years_dictionary()))
