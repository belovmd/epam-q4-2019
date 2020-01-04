import unittest
from rss_reader.reader import parse_arguments


class TestArgparse(unittest.TestCase):
    """test argparse functions"""
    def test_arg_parse(self):
        parser = parse_arguments(['some_url', '--limit', '5', '--json', '--verbose', '--version',
                                  '--date', '20191210', '--output-path', 'some_path', '--to-epub', '--to-html'])
        self.assertEqual(parser.url, 'some_url')
        self.assertTrue(parser.limit == 5)
        self.assertTrue(parser.json)
        self.assertTrue(parser.verbose)
        self.assertTrue(parser.version)
        self.assertEqual(parser.date, '20191210')
        self.assertEqual(parser.output_path, 'some_path')
        self.assertTrue(parser.to_epub)
        self.assertTrue(parser.to_html)


    def test_empty_arg_parse(self):
        parser = parse_arguments(['some_url'])
        self.assertEqual(parser.url, 'some_url')
        self.assertFalse(parser.limit)
        self.assertFalse(parser.json)
        self.assertFalse(parser.verbose)
        self.assertFalse(parser.version)
        self.assertFalse(parser.date)
        self.assertFalse(parser.to_epub)
        self.assertFalse(parser.to_html)

