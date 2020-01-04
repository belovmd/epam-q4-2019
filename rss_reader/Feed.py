import feedparser
from rss_reader.FeedTitle import FeedTitle
from rss_reader.Entry import Entry
import rss_reader.ebook as ebook
import json
import datetime
import os


class Feed:
    """Class of one RSS feed
    Feed consist of two blocs: FeedTitle (title, link and access date) and Entries. Entries is list of objects "Entry"
    class.
    Class include those functions:
     - print() - print feed descriptions and all entries in easy to read format. If --limit parameter set, function will
      print only established number of entries.
    -print_json() -  print feed in JSON style. If --limit parameter set, function will print only established number of
     entries.
    -caching - all news will cached into cache.txt'
    """

    feed_url = ""

    def __init__(self, url, limit):
        self.feed_url = url
        the_feed = feedparser.parse(self.feed_url)

        self.no_entries_in_feed = False if the_feed.entries else True

        self.feed_title = FeedTitle(the_feed)
        self.entries = []
        entry_number = 1
        for entry in the_feed.entries:
            if limit and entry_number > limit:
                break
            self.entries.append(Entry(entry))
            entry_number += 1

        self.json_data = {
            'access_time': str(datetime.datetime.now()),
            'feed_url': self.feed_url,
            'published': self.feed_title.published,
            'source': self.feed_title.title,
            'feed_description': self.feed_title.description,
            'entries': [entry.output_to_json() for entry in self.entries]
        }

    def print(self):
        """Print Feed (Title and every Entry) in easy to read format"""
        end_of_feed_title = '\n==========================\n'
        end_of_entry = '\n___________________________\n'
        print(*self.feed_title.output(), sep='\n', end=end_of_feed_title)
        for entry in self.entries:
            print(*entry.output(), sep='\n', end=end_of_entry)

    def print_json(self):
        """Print Feed (Title end Entries) in json format
         JSON structure:
        {
            'access_time': 01.01.1900 00:00:00,
            'feed_url': example.com/rss,
            'published': 01.01.2019 00:00:00,
            'source': , example.com,
            'feed_description': self.feed_title.description,
            'entries':
            [
                {
                    'title': 'News title',
                    'link': 'example.com/news1.html',
                    'description': 'News summary',
                    'img_links:':
                        [
                            img_saver.com/1234.png,
                            ...
                        ],
                    'published': 01.01.2018 00:00:00,
                },
                {
                    ...
                }
             ]
        }
        """
        print(self.json_data)

    def caching(self):
        """Write Feed to cache file (in JSON format). Cache file is list of Feed JSONs """
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        with open(curr_dir + '/cache.txt', 'a') as cache_file:
            cache_file.write(json.dumps(self.json_data) + '\n')

    def create_epub(self, path):
        """Create epub file from all entries in the feed. It contains only text information"""
        ebook.generate_epub(self, path)

    def create_html(self, path):
        """Create html file """
        ebook.generate_html(self, path)
