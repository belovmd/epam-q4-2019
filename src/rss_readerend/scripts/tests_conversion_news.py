from contextlib import redirect_stdout
import datetime
from io import StringIO
import json
import os
from scripts.conversion_news import read_news_from_cache
from scripts.conversion_news import unpack_json
from scripts.conversion_news import unpack_news
from scripts.conversion_news import filter_news_by_date
import unittest


class TestUnpackWithDate(unittest.TestCase):

    def test_unpack(self):
        user_date = datetime.date(2019, 12, 5)
        news = {'Devastating factory fire kills at least 43 in Indian capital':
                ["Sat, 07 Dec 2019 23:23:22 -0500", '20191207'],
                '50 Great Gadget and Gear Gifts for the Holidays':
                    ['Sat, 05 Dec 2019 23:23:22 -0500', '20191205']}
        self.assertEqual(filter_news_by_date(user_date, news), ({'50 Great Gadget and Gear Gifts for the Holidays':
                                                                ['Sat, 05 Dec 2019 23:23:22 -0500', '20191205']}, 1))


class TestUnpackJson(unittest.TestCase):

    def test(self):
        news = {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date'],
                'Europe': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date']}
        self.assertEqual(unpack_json(news, 1),
                         {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date']
                          })


class TestReadNews(unittest.TestCase):
    def test(self):
        FILE_NAME = 'test.json'
        json_data = {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date'],
                     'Europe': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date']}
        with open(FILE_NAME, 'w') as file:
            json.dump(json_data, file)
        read_data = read_news_from_cache(FILE_NAME)
        os.remove(FILE_NAME)
        self.assertEqual(read_data, json_data)


class TestUnpackNews(unittest.TestCase):

    def setUp(self):
        self.news = {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date'],
                     'Europe': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', None, 'description', 'date']
                     }
        self.output = StringIO()

    def test_with_limit(self):
        with redirect_stdout(self.output):
            unpack_news(self.news, limit=1)
        self.assertEqual(self.output.getvalue(), 'Title: India\n' +
                         'Date: Sat, 07 Dec 2019 05:17:55 -0500\n\n' +
                         'Description: description\n\n\n' +
                         'Links:\n' +
                         '[1] url (link)\n' +
                         '[2] img_url (img)\n\n\n\n')

    def test_with_main_title(self):
        with redirect_stdout(self.output):
            unpack_news(self.news, limit=1, main_title='Yahoo')

        self.assertEqual(self.output.getvalue(), '\nFeed: Yahoo\n\n' +
                         'Title: India\n' +
                         'Date: Sat, 07 Dec 2019 05:17:55 -0500\n\n' +
                         'Description: description\n\n\n' +
                         'Links:\n' +
                         '[1] url (link)\n' +
                         '[2] img_url (img)\n\n\n\n')


if __name__ == '__main__':
    unittest.main()
