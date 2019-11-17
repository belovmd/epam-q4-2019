def list_to_dict(lst):
    dct = {elem: lst.count(elem) for elem in lst}
    return dct


def histogram(dct, file_name):
    maximal = 1
    for value in dct.values():
        if maximal < value:
            maximal = value

    with open(file_name, "w") as file_to_write:
        while maximal > 0:
            for value in dct.values():
                if value >= maximal:
                    file_to_write.write("#     ")
                else:
                    file_to_write.write("      ")
            file_to_write.write("\n")
            maximal = maximal - 1
        for key in dct.keys():
            file_to_write.write(str(key) + " " * (6-len(key)))


year_lst = []
rating_lst = []
file = open("ratings.list")
top = open("top250_movies.txt", "w")
for i, line in enumerate(file):
    if i > 277:
        break
    if i > 27:
        movie = line.strip().split(None, 3)[3].rsplit(" ", 1)
        title = movie[0]
        top.write(title + "\n")

        rating_lst.append(line.strip().split(None, 3)[2])
        year_lst.append(movie[1][1:5])

file.close()
top.close()

histogram(list_to_dict(sorted(rating_lst)), "ratings.txt")
histogram(list_to_dict(sorted(year_lst)), "years.txt")
