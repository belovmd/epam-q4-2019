from collections import OrderedDict


def open_file(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("File not found")

    list = []
    with file:
        for i in range(28):
            file.readline()
        for i in range(250):
            movie = [i for i in file.readline().strip().split() if i]
            list.append({"title": ' '.join(movie[3:-1]),
                         "ratings": float(movie[2]),
                         "year": int(movie[-1][1:5]), })

    with open('top250_movies.txt', 'w') as file:
        for i in list:
            file.write(i["title"] + '\n')

    years = {}
    for i in list:
        if i["year"] in years:
            years[i["year"]] += 1
        else:
            years[i["year"]] = 1

    Dict1 = OrderedDict(sorted(years.items()))
    with open('years.txt', 'w') as file:
        for key in Dict1.keys():
            file.write(str(key) + ' ')
            for i in range(Dict1[key]):
                file.write('#')
            file.write('\n')

    rating = {}
    for i in list:
        if i["ratings"] in rating:
            rating[i["ratings"]] += 1
        else:
            rating[i["ratings"]] = 1

    Dict2 = OrderedDict(sorted(rating.items()))
    with open('ratings.txt', 'w') as file:
        for key in Dict2.keys():
            file.write(str(key) + ' ')
            for i in range(Dict2[key]):
                file.write('#')
            file.write('\n')


open_file("ratings.list")
