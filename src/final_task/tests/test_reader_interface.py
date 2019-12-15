import rss_reader
import unittest


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = rss_reader.create_parser()

    def test_minimal_input(self):
        parsed = self.parser.parse_args(["https://news.yahoo.com/rss"])
        self.assertEqual(parsed.source, "https://news.yahoo.com/rss")

    def test_maximum_input(self):
        parsed = self.parser.parse_args(
            [
                "https://news.yahoo.com/rss --verbose --json --version "
                "--limit 42"
            ]
        )
        self.assertEqual(
            parsed.source,
            "https://news.yahoo.com/rss --verbose --json --version --limit 42",
        )


if __name__ == "__main__":
    unittest.main()
