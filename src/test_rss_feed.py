import rss_feed
from rss_feed import Rss_feed
import unittest


class Test_rss_feed(unittest.TestCase):
    def setUp(self):
        self.xml_string_rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/"  >
  <channel>
    <title>Chanel title</title>
    <link>https://dot.com</link>
    <description><![CDATA[channel description]]></description>
    <pubDate>Mon, 02 Dec 2019 08:59:59 GMT</pubDate>
    <item>
      <title><![CDATA[Item1 title]]></title>
      <link>https://dot.com/1</link>
      <description><![CDATA[Item description]]></description>
      <pubDate>Mon, 02 Dec 2019 08:28:46 GMT</pubDate>
    </item>
  </channel>
</rss>"""
        self.xml_string_atom = """<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <id>https://dot.com/</id>
    <title>Feed title</title>
    <updated>2019-12-02T08:51:07.753Z</updated>
    <link rel="alternate" href="https://dot.com/"/>
    <subtitle>Feed subtitle</subtitle>
    <entry>
        <title type="html"><![CDATA[Entry title]]></title>
        <link href="https://dot.com/1">
        </link>
        <updated>2019-12-02T08:39:00.000Z</updated>
        <summary type="html"><![CDATA[Entry summary]]></summary>
    </entry>
</feed>"""

    def test_rss_feed_class_creation(self):
        """Test creation of Rss_feed class"""

        feed = Rss_feed()
        self.assertIsNotNone(feed)

    def test_rss_feed_parse_empty_string(self):
        """Test parsing empty string"""

        feed = Rss_feed()
        feed.parse_xml_string("")
        self.assertEqual(feed.rss_format_id, rss_feed.UNKNOWN_FOMRAT)

    def test_rss_feed_rss_format(self):
        """Test detecting rss format"""

        feed = Rss_feed()
        feed.parse_xml_string(self.xml_string_rss)
        self.assertEqual(feed.rss_format_id, rss_feed.RSS_FOMRAT)

    def test_rss_feed_rss_elements(self):
        """Test extracting elements in rss format"""

        feed = Rss_feed()
        feed.parse_xml_string(self.xml_string_rss)
        self.assertEqual(len(feed.entries), 1)
        title, timestamp, link, summary = (
            feed.parse_entry(feed.entries[0]))
        self.assertEqual(title, 'Item1 title')
        self.assertEqual(timestamp, 'Mon, 02 Dec 2019 08:28:46 GMT')
        self.assertEqual(link, 'https://dot.com/1')
        self.assertEqual(summary, 'Item description')

    def test_rss_feed_atom_format(self):
        """Test detecting atom format"""

        feed = Rss_feed()
        feed.parse_xml_string(self.xml_string_atom)
        self.assertEqual(feed.rss_format_id, rss_feed.ATOM_FOMRAT)

    def test_rss_feed_atom_elements(self):
        feed = Rss_feed()
        feed.parse_xml_string(self.xml_string_atom)
        self.assertEqual(len(feed.entries), 1)
        title, timestamp, link, summary = (
            feed.parse_entry(feed.entries[0]))
        self.assertEqual(title, 'Entry title')
        self.assertEqual(timestamp, '2019-12-02T08:39:00.000Z')
        self.assertEqual(link, 'https://dot.com/1')
        self.assertEqual(summary, 'Entry summary')


if __name__ == '__main__':
    unittest.main()
