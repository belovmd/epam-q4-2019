from collections import defaultdict
import json

"""Unpack json into strings(news format)
Default quantity of news is 50 in RSS format"""


def unpack_news(news, limit, main_title=None):
    DATE_INDEX = 0
    LINK_INDEX = 1
    IMG_INDEX = 2
    DESCRIPTION_INDEX = 3
    try:
        keys = list(news.keys())
    except AttributeError:
        print('New not found')
    else:
        if limit != 0 or limit is not None:
            if main_title:
                print('\nFeed: {0}\n'.format(main_title))
            for one_news in range(limit):
                title = keys[one_news]
                info = news[title]
                pub_date = info[DATE_INDEX]
                link = info[LINK_INDEX]
                description = info[DESCRIPTION_INDEX]
                img_link = info[IMG_INDEX]
                print('Title: {0}'.format(title))
                print('Date: {0}\n'.format(pub_date))
                print('Description: {0}\n\n'.format(description))
                print('Links:')
                if img_link:
                    print('[1] {0} (link)'.format(link))
                    print('[2] {0} (img)\n\n\n'.format(img_link))
                else:
                    print('[1] {0} (link)\n\n\n'.format(link))
        else:
            print('\nNews not found\n')


"""Json output.
News is news in json format.
limit is quantity of  news, which prints"""


def unpack_json(news, limit):
    limit_news = defaultdict(list)
    news_keys = list(news.keys())
    for one_news in range(limit):
        key = news_keys[one_news]
        limit_news[key].extend(news[key])
    print(dict(limit_news))
    return dict(limit_news)


"""User_date is date from user
News is news in json format.
Function returns sorted news by date"""


def filter_news_by_date(user_date, news):
    user_date = user_date.strftime('%Y%m%d')
    new_news = defaultdict(list)
    try:
        for one_news, info in news.items():
            if user_date in info:
                new_news[one_news].extend(info)
        limit = len(new_news)

    except AttributeError:
        pass
    except TypeError:
        pass
    else:
        return dict(new_news), limit


"""Function reads data from local storage in json format.
Default name of local storage is news.json.
File argument only for tests.
You should not touch him"""


def read_news_from_cache(file_name='news.json'):
    try:
        with open(file_name, 'r') as file:
            news = json.load(file)
    except FileNotFoundError:
        print("You don't have data in local storage\n"
              "First of all you should see data from sites\n"
              "For example: rss-reader https://news.yahoo.com/rss/")
    else:
        return news
