"""RSS reader which is responsible for everything
associated with parsing news"""

import feedparser
import json
from ebooklib import epub
from datetime import datetime
from RssReader import logger
from lxml import html


class RssParser(object):
    feed_url = ""
    news = {}

    def __init__(self, params_url, qty=1):
        self.feed_url = params_url
        self.qty = qty
        self.parse()

    def parse(self):
        """Function that parse news"""
        the_feed = feedparser.parse(self.feed_url)
        logger.log.info('Start')
        print("Getting Feed Data")
        print(the_feed.feed.get("title", "") + "\n")

        for feed_entry in the_feed.entries:
            if self.qty:
                self.qty -= 1
                title = ("Title:" + feed_entry.get("title", ""))
                date = (feed_entry.get("published", ""))
                link = ("Link:" + feed_entry.get("link", "") + "\n")
                description = feed_entry.get("description", "")
                tree1 = html.fromstring(description)
                text1 = tree1.xpath('//p/text()')

                self.news[title] = [date, link, text1]

    def convert_to_json(self):
        """Function that converts news to json format"""
        logger.log.info('Convert to json')
        parsed = json.dumps(self.news, indent=4, sort_keys=True)
        return parsed

    def printer(self):
        """Function that prints news"""
        logger.log.info('Print news')
        for item in self.news:
            print('\n')
            print(item)
            for element in self.news[item]:
                print(element)

    def to_epub(self, way=''):
        """Function that converts news to epub format"""
        try:
            logger.log.info('Convert to epub')
            book = epub.EpubBook()

            # set metadata
            book.set_identifier('id123456')
            book.set_title('news')
            book.set_language('en')

            book.add_author('Rashkevich Vadim')
            book.add_author('Rashkevich Vadim', file_as='Epub', role='ill', uid='coauthor')

            # create chapter
            chapter_file_counter = 1
            ep = ""
            c1 = epub.EpubHtml(title='Intro', file_name='{}.xhtml'.format(chapter_file_counter), lang='hr')
            for item in self.news:
                ep += str(item) + '<br>'
                for element in self.news[item]:
                    ep += str(element) + '<br>'
                chapter_file_counter += 1
                c1.content = ep

                # add chapter
                book.add_item(c1)

            # define Table Of Contents
            book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),
                        (epub.Section('Simple book'),
                         (c1,))
                        )

            # add default NCX and Nav file
            book.add_item(epub.EpubNcx())
            book.add_item(epub.EpubNav())

            # define CSS style
            style = 'BODY {color: white;}'
            nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

            # add CSS file
            book.add_item(nav_css)

            # basic spine
            book.spine = ['nav', c1]

            # write to the file
            file_name = way + '/book1.epub'
            epub.write_epub(file_name, book, {})
            print('Successful')

        except Exception:
            raise Exception('Error converting to EPUB')

    def cache_news(self):
        """Function that caches news"""
        try:
            with open("database.txt", 'r+') as f:
                json_dict = json.loads(f.read())
                f.seek(0, 0)
                logger.log.info('Cache news')
                for i in self.news:
                    datetime_object = datetime.strptime(self.news[i][0], '%a, %d %b %Y %H:%M:%S %z')
                    date = str(datetime_object.year) + str(datetime_object.month) + str(datetime_object.day)
                    if date not in json_dict:
                        json_dict[date] = []
                        json_dict[date].append(i)
                    else:
                        if i not in json_dict[date]:
                            json_dict[date].append(i)
                f.write(json.dumps(dict(json_dict), indent=4, ensure_ascii=False))
        except FileNotFoundError:
            with open("database.txt", 'w+') as f:
                json_dict = {}
                logger.log.info('Cache news')
                for i in self.news:
                    datetime_object = datetime.strptime(self.news[i][0], '%a, %d %b %Y %H:%M:%S %z')
                    date = str(datetime_object.year) + str(datetime_object.month) + str(datetime_object.day)
                    if date not in json_dict:
                        json_dict[date] = []
                        json_dict[date].append(i)
                    else:
                        if i not in json_dict[date]:
                            json_dict[date].append(i)
                f.write(json.dumps(dict(json_dict), indent=4, ensure_ascii=False))
