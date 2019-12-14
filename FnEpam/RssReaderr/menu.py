"""Main module"""

import argparse
from RssReader.getting_news import get_cached_news
from RssReader.rssaggregator import RssParser


def main():
    try:
        parser = argparse.ArgumentParser(description='Test')

        parser.add_argument("--limit", action='store', dest='limit',
                            help='Simple value', default=1)
        parser.add_argument("--verbose", action="store_true",
                            help="increase output verbosity")
        parser.add_argument("--version", action="store_true",
                            help="version of this program")
        parser.add_argument("--json", action="store_true",
                            help="convert to json")
        parser.add_argument("--epub", action="store_true",
                            help="convert to epub")
        parser.add_argument("--date", action="store", dest='date',
                            help="get caching news by date")
        parser.add_argument("--output", action="store",
                            help="name of directory")
        parser.add_argument('string', metavar='S', type=str)

        args = parser.parse_args()

        if args.verbose:
            with open("sample.log", 'r+') as f:
                date = f.read()
                print(date)
        elif args.version:
            print("iteration 4")
        elif args.json:
            print(RssParser(args.string, int(args.limit)).convert_to_json())
        elif args.epub:
            if args.output:
                RssParser(args.string, int(args.limit)).to_epub(args.output)
            else:
                RssParser(args.string, int(args.limit)).to_epub()
        elif args.date:
            RssParser(args.string, int(args.limit)).cache_news()
            print(get_cached_news(args.date))
        elif args.limit:
            obj = RssParser(args.string, int(args.limit))
            obj.cache_news()
            obj.printer()
        else:
            obj = RssParser(args.string, int(args.limit))
            obj.cache_news()
            obj.printer()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
