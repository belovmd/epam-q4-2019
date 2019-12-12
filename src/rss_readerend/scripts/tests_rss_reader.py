import json
from scripts.rss_reader import retrieve_from_cache
import unittest


class TestRetrieveFromCache(unittest.TestCase):
    def test_without_date(self):
        FILE_NAME = 'test.json'
        json_data = {'India': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date'],
                     'Europe': ["Sat, 07 Dec 2019 05:17:55 -0500", 'url', 'img_url', 'description', 'date']}
        with open(FILE_NAME, 'w') as file:
            json.dump(json_data, file)
        news, limit = retrieve_from_cache(file=FILE_NAME)
        self.assertEqual(news, json_data)
        self.assertEqual(limit, 2)


if __name__ == '__main__':
    unittest.main()
