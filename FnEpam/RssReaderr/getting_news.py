import json


def get_cached_news(date):
    """Function that return cached news from given date"""
    try:
        cached_news = []
        with open("database.txt", 'r') as f:
            json_dict = json.loads(f.read())
            if date in json_dict:
                for news in json_dict[date]:
                    cached_news.append(news)
                return cached_news
    except (FileNotFoundError, Exception) as e:
        raise Exception('Error getting cached news: {}'.format(e))
