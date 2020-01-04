import unittest
import os
from rss_reader.Feed import Feed


class TestFeedClass(unittest.TestCase):
    def setUp(self):
        self.test_feed = os.getcwd() + r'/example_feed.xml'

    def test_feed_title(self):
        feed = Feed(self.test_feed, limit=None)
        feed_title = feed.feed_title.title
        self.assertEqual(feed_title, 'Yahoo News - Latest News & Headlines')

    def test_feed_link(self):
        feed = Feed(self.test_feed, limit=None)
        feed_title = feed.feed_title.link
        self.assertEqual(feed_title, 'https://www.yahoo.com/news')

    def test_feed_description(self):
        feed = Feed(self.test_feed, limit=None)
        feed_title = feed.feed_title.description
        self.assertEqual(feed_title, 'The latest news and headlines from Yahoo! News. Get breaking news stories and'
                                     ' in-depth coverage with videos and photos.')

    def test_feed_publish_time(self):
        feed = Feed(self.test_feed, limit=None)
        feed_publish_time = feed.feed_title.published
        self.assertEqual(feed_publish_time, 'Wed, 01 Jan 2020 12:24:03 -0500')

    def test_entry_title(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_title = feed.entries[0].title
        self.assertEqual(feed_entry_title, 'PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad')

    def test_entry_link(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_link = feed.entries[0].link
        self.assertEqual(feed_entry_link,
                         'https://news.yahoo.com/photos-iraqi-shiites-break-into-us-embassy-in-baghdad-132418054.html')

    def test_entry_publish_time(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_publish_time = feed.entries[0].published
        self.assertEqual(feed_entry_publish_time, 'Tue, 31 Dec 2019 08:24:18 -0500')

    def test_entry_description(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_descr = feed.entries[0].description
        self.assertEqual(feed_entry_descr, ' [image 1: PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad] Dozens'
                                           ' of Iraqi Shiite militiamen and their supporters broke into the U.S.'
                                           ' Embassy compound in Baghdad on Tuesday, smashing a main door and setting'
                                           ' fire to a reception area, prompting tear gas and sounds of gunfire,'
                                           ' angered over deadly U.S. airstrikes targeting the Iran-backed militia.'
                                           '  An Associated Press reporter at the scene saw flames rising from inside'
                                           ' the compound and at least three U.S. soldiers on the roof of the main'
                                           ' embassy building.  It followed deadly U.S. airstrikes on Sunday that'
                                           ' killed 25 fighters of the Iran-backed militia in Iraq, the Kataeb'
                                           ' Hezbollah.')

    def test_entry_img_link(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_img_link = feed.entries[0].img_links
        self.assertEqual(feed_entry_img_link,
                         ['http://l.yimg.com/uu/api/res/1.2/Dbv76oxlCUoDEOvu5BGDFg--/YXBwaWQ9eXRhY2'
                          'h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/creat'
                          'r-uploaded-images/2019-12/6abf3810-2bd0-11ea-9feb-8bbd689da111'])

    def test_entry_img_title(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_img_title = feed.entries[0].img_titles
        self.assertEqual(feed_entry_img_title, ['PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad'])

    def test_entry_output(self):
        feed = Feed(self.test_feed, limit=None)
        feed_entry_output = feed.entries[0].output()
        self.assertEqual(feed_entry_output, ['PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad',
                                             'Подробнее: https://news.yahoo.com/photos-iraqi-shiites-break-into-us-emba'
                                             'ssy-in-baghdad-132418054.html',
                                             '\n [image 1: PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad]'
                                             ' Dozens of Iraqi Shiite militiamen and their supporters broke into the'
                                             ' U.S. Embassy compound in Baghdad on Tuesday, smashing a main door and'
                                             ' setting fire to a reception area, prompting tear gas and sounds of'
                                             ' gunfire, angered over deadly U.S. airstrikes targeting the Iran-backed'
                                             ' militia.  An Associated Press reporter at the scene saw flames rising'
                                             ' from inside the compound and at least three U.S. soldiers on the roof of'
                                             ' the main embassy building.  It followed deadly U.S. airstrikes on Sunday'
                                             ' that killed 25 fighters of the Iran-backed militia in Iraq, the Kataeb'
                                             ' Hezbollah.\n',
                                             '[1]: http://l.yimg.com/uu/api/res/1.2/Dbv76oxlCUoDEOvu5BGDFg--/YXBwaWQ9e'
                                             'XRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3.amazonaws.com/'
                                             'creatr-uploaded-images/2019-12/6abf3810-2bd0-11ea-9feb-8bbd689da111',
                                             'Дата публикации: Tue, 31 Dec 2019 08:24:18 -0500'])

    def test_entry_output_to_json(self):
        feed = Feed(self.test_feed, limit=None)
        entry_json = feed.entries[0].output_to_json()
        self.assertEqual(entry_json, {'description': ' [image 1: PHOTOS: Iraqi Shiites break into U.S. Embassy in '
                                                     'Baghdad] Dozens of Iraqi Shiite militiamen and their supporters'
                                                     ' broke into the U.S. Embassy compound in Baghdad on '
                                                     'Tuesday, smashing a main door and setting fire to a reception '
                                                     'area, prompting tear gas and sounds of gunfire, angered over '
                                                     'deadly U.S. airstrikes targeting the Iran-backed militia.  An '
                                                     'Associated Press reporter at the scene saw flames rising from '
                                                     'inside the compound and at least three U.S. soldiers on the '
                                                     'roof of the main embassy building.  It followed deadly U.S. '
                                                     'airstrikes on Sunday that killed 25 fighters of the '
                                                     'Iran-backed militia in Iraq, the Kataeb Hezbollah.',
                                      'img_links:': [
                                          'http://l.yimg.com/uu/api/res/1.2/Dbv76oxlCUoDEOvu5BGDFg'
                                          '--/YXBwaWQ9eXRhY2h5b247aD04Njt3PTEzMDs-/https://media-mbst-pub-ue1.s3'
                                          '.amazonaws.com/creatr-uploaded-images/2019-12/6abf3810-2bd0-11ea-9feb'
                                          '-8bbd689da111'],
                                      'link': 'https://news.yahoo.com/photos-iraqi-shiites-break-into-us-embassy-in'
                                              '-baghdad-132418054.html',
                                      'published': 'Tue, 31 Dec 2019 08:24:18 -0500',
                                      'title': 'PHOTOS: Iraqi Shiites break into U.S. Embassy in Baghdad'})

    def test_entries_limit(self):
        feed = Feed(self.test_feed, limit=4)
        self.assertEqual(len(feed.entries), 4)

    def test_if_limit_more_than_entries_count(self):
        feed = Feed(self.test_feed, limit=9999)
        self.assertEqual(len(feed.entries), 50)

    def test_no_entries_in_the_feed(self):
        feed = Feed('http://www.onliner.by', limit=None)
        self.assertTrue(feed.no_entries_in_feed)
