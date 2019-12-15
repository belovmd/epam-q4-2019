import errors
import rss_reader as rr
import testdata.small_valid_parsed_response as svpr
import unittest


class VersionTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(rr.version(), "v0.4.0")


class RequestsTest(unittest.TestCase):
    def test_invalid_link(self):
        with self.assertRaises(errors.FetchRssError):
            rr.fetch_rss("sdfsdfsdf")

    def test_broken_link(self):
        with self.assertRaises(errors.FetchRssError):
            rr.fetch_rss("https://epam/rabbitjunkZ123.com")

    def test_valid_link(self):
        self.assertIn(
            '<?xml version="1.0" encoding="UTF-8"?>',
            rr.fetch_rss("https://news.yahoo.com/rss"),
        )


class elementTreeTest(unittest.TestCase):
    def setUp(self):
        with open("testdata/valid.xml", "rt") as f:
            self.good_xml = f.read()
        with open("testdata/invalid.xml", "rt") as f:
            self.bad_xml = f.read()
        with open("testdata/small_valid.xml", "rt") as f:
            self.small_valid_xml = f.read()
        self.small_valid_parsed_response_channel = svpr.title
        self.small_valid_parsed_response_items = svpr.items

    def test_small_valid(self):
        self.assertEqual(
            rr.parse_xml(self.small_valid_xml),
            (
                self.small_valid_parsed_response_channel,
                self.small_valid_parsed_response_items,
            ),
        )


if __name__ == "__main__":
    unittest.main()
