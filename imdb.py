import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image


def opener(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print('File does not exist or not found')

    lst = []
    with file:
        for i in range(28):
            file.readline()
        for i in range(250):
            film = [i for i in file.readline().strip().split() if i]
            lst.append({"title": ' '.join(film[3:-1]),
                        "ratings": float(film[2]),
                        "year": int(film[-1][1:5]), })

    with open('top250_movies.txt', 'w') as file:
        for i in lst:
            file.write(i['title'] + '\n')
    years = {}
    for i in lst:
        if i["year"] in years:
            years[i["year"]] += 1
        else:
            years[i["year"]] = 1
    plt.bar(*zip(*years.items()))
    plt.savefig('result_years.png')
    plt.show()

    rating = {}
    for i in lst:
        if i["ratings"] in rating:
            rating[i["ratings"]] += 1
        else:
            rating[i["ratings"]] = 1
    rating = pd.DataFrame.from_dict(rating, orient='index')
    fig = rating.plot(kind='bar')
    fig.get_figure().savefig('result_rating.png')
    with Image.open('result_rating.png') as img:
        img.show()


opener('ratings.list')
