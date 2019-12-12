from scripts.rss_parser import formatted_date
import unittest


class TestFormattedDate(unittest.TestCase):
    def test(self):
        input_date = 'Mon, 09 Dec 2019 09:38:58 -0500'
        output_date = '20191209'
        self.assertEqual(formatted_date(input_date), output_date)


if __name__ == '__main__':
    unittest.main()
