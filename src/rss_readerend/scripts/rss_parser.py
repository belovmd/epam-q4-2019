from bs4 import BeautifulSoup
from collections import defaultdict
import json
import re
import requests
from requests.exceptions import HTTPError

""" Function finds news on site  and return news, main_title,
writes news in local storage in json format.
Json format {title:[pub_date, link, img_url, description,formatted date]}
Formatted date: Mon, 09 Dec 2019 06:21:51 -0500" = 20191209"""


def find_news(url):
    news = defaultdict(list)
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_exc:
        print('Http error {0}'.format(http_exc))
    except Exception as exc:
        print('Other error {0}'.format(exc))
    else:
        soup = BeautifulSoup(response.text, 'xml')
        main_title = soup.find('title').text
        items = soup.find_all('item')
        for item in items:
            title = item.find('title').text
            pub_date = item.find('pubDate').text
            link = item.find('link').text
            description = item.find('description')

            """Without BeautifulSoup data is not xml"""

            description_soup = BeautifulSoup(description.text, 'xml')
            description = re.split(r'[</a>,<p>]', description_soup.text)
            description = ''.join(description).strip('\n')
            form_date = formatted_date(pub_date)
            media_content = item.find('media:content')
            img_url = None if media_content is None else media_content.get('url')
            news[title].extend([pub_date, link, img_url, description, form_date])

        FILE_NAME = 'news.json'

        """r+ not clear file,
        w+ -  first of the all clear file(JsonDecodeError)"""

        try:
            with open(FILE_NAME, 'r') as file:
                data = json.load(file)
                data.update(news)
            with open(FILE_NAME, 'w') as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError:
            with open(FILE_NAME, 'w') as file:
                json.dump(news, file, indent=2)

        return news, main_title


"""Date is pub_date from site.
Function converts pub_date to format 20191209
Formatted date: Mon, 09 Dec 2019 06:21:51 -0500" = 20191209"""


def formatted_date(date):
    months = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
              'Sep': '9', 'Oct': '10',
              'Nov': '11', 'Dec': '12'}
    START_YEAR = 11
    END_YEAR = 15
    START_MONTH = 8
    END_MONTH = 10
    START_DIGIT = 5
    END_DIGIT = 7
    for month, month_number in months.items():
        new_date = date.replace(month, month_number)
        if new_date == date:
            continue
        else:
            year = new_date[START_YEAR:END_YEAR]
            month = new_date[START_MONTH:END_MONTH]
            digit = new_date[START_DIGIT:END_DIGIT]
            new_date = year + month + digit
            return new_date


if __name__ == '__main__':
    find_news('https://news.yahoo.com/rss/')
    news, title = find_news('https://habr.com/ru/rss/all/all/')
    print(news)
    print(title)
