import argparse
import datetime
import logging
from scripts.conversion_news import read_news_from_cache
from scripts.conversion_news import unpack_json
from scripts.conversion_news import unpack_news
from scripts.conversion_news import filter_news_by_date
from scripts.create_fb2 import create_fb2
from scripts.rss_parser import find_news

"""Functions checks data by format YearMonthDay(20191209)"""


def valid_date(date):
    try:
        return datetime.datetime.strptime(date, '%Y%m%d')
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(
            date)
        raise argparse.ArgumentTypeError(msg)


"""Function parses the arguments from use and returns it"""


def parse_arguments():
    parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')
    parser.add_argument('source', help='RRS URL or date if want to use --date', nargs='?')
    parser.add_argument('--verbose', action='store_true', help='Outputs verbose status message')
    parser.add_argument('--version', action='version', version='%(prog)s 0.4', help='Print version info')
    parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    parser.add_argument('--limit', type=int, help='Limit topics if this parameter provided')
    parser.add_argument('--date', type=valid_date, help='Print news by publication date')
    parser.add_argument('--output-path', dest='output_path', type=str, help='Path to save fb2')
    parser.add_argument('--to-fb2', dest='to_fb2', action='store_true', help='Conversion news in fb.2')

    return parser.parse_args()


"""Function checks the arguments compatibility"""


def validate_arguments(args):
    if args.limit is not None and args.limit < 0:
        print('Limit must be >0')
        return False
    if args.json and args.output_path is not None:
        print('ArgumentsError: You should use --json without --out-path')
        return False
    if args.source is not None and args.source == '':
        print('You should give the rss_url')
        return False
    if args.output_path and not args.to_fb2:
        print('You should use --output-path with --to-fb2')
        return False
    return True


"""Function takes arguments from user and processes it"""


def process_arguments(args):
    news = None
    max_limit = None
    if args.source == 'date':
        if args.date:
            news, max_limit = retrieve_from_cache(args.date)
            logging.debug(args, max_limit)
    else:
        try:
            news, title, max_limit = retrieve_from_url(
                args.source)
        except TypeError:
            pass
    if args.to_fb2:
        dump_news_to_fb2(news, args.output_path)
        logging.debug(args, max_limit)

    else:
        dump_news_to_stdout(news, args.limit, max_limit, as_json=args.json)
        logging.debug(args, max_limit)


"""Functions prints news in stdout"""


def dump_news_to_stdout(news, limit, max_limit, as_json=None,
                        title=None):
    if as_json:
        if limit:
            if max_limit < limit:
                print('{0} news on site'.format(max_limit))
            else:
                unpack_json(news, limit)
        else:
            unpack_json(news, max_limit)
    else:
        if limit:
            if max_limit < limit:
                print('{0} news on site'.format(max_limit))
            else:
                unpack_news(news, limit, title)
        else:
            unpack_news(news, max_limit, title)


"""Function converts news to fb2 format"""


def dump_news_to_fb2(news, output_path):
    create_fb2(news, output_path)


def retrieve_from_url(url):
    try:
        news, title = find_news(url)
    except TypeError:
        pass
    else:
        max_limit = len(news)
        return news, title, max_limit


"""Data in Json format in the local storage file 'news.json or news from cite
Don't touch file argument.
"""


def retrieve_from_cache(date=None, file='news.json'):
    first_news = read_news_from_cache(file)
    max_limit = len(first_news)
    if date:
        news, limit = filter_news_by_date(user_date=date, news=first_news)
        return news, limit
    else:
        return first_news, max_limit


"""Function retrieve news from cite and return this news and it quantity"""


def retrieve_json(url, limit=None):
    NEWS_INDEX = 0
    try:
        news = dict(find_news(url)[NEWS_INDEX])
    except TypeError:
        pass
    else:
        if limit:
            news = unpack_json(news, limit)
            max_limit = len(news)
            return news, max_limit

        else:
            max_limit = len(news)
            return news, max_limit


"""Function takes url of cite and path to saves news from sites in fb2 format
Function returns this news and path"""


def conversion_to_fb2_with_url(url, path=None):
    NEWS_INDEX = 0
    news = dict(find_news(url)[NEWS_INDEX])
    return news, path


"""CLI"""


def main():
    args = parse_arguments()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)
    logging.debug(args)
    if not validate_arguments(args):
        return -1
    process_arguments(args)


if __name__ == '__main__':
    main()
