import argparse
import logging
import json
import time
from rss_reader.Feed import Feed
from rss_reader import exceptions
import httplib2
import urllib
import sys
import os


def check_if_url_valid(url):
    h = httplib2.Http()
    try:
        resp = h.request(url, 'HEAD')
    except httplib2.ServerNotFoundError:
        logging.error('ServerNotFoundError')
        raise exceptions.ServerNotFoundError("Not valid server. Please, check site address")
    else:
        if int(resp[0]['status']) > 400:
            logging.error('PageDoesNotExistError')
            raise exceptions.PageDoesNotExistError("Page does not exist. Please, check URL")
        elif int(resp[0]['status']) == 404:
            logging.error('FeedNotFoundError')
            raise exceptions.FeedNotFoundError('There is not such page on this server Please check URL')
        return True


def check_internet_connection():
    check_host = 'http://google.com'
    try:
        urllib.request.urlopen(check_host)
        return True
    except Exception:
        logging.error('NoInternetConnectionError')
        raise exceptions.NoInternetConnectionError('Please, check internet connection')


def display_cache(url_to_show, date_to_show):
    try:
        date_to_show = time.strptime(date_to_show, '%Y%m%d')
    except ValueError:
        logging.error('InvalidDateError')
        raise exceptions.InvalidDateError('Wrong date. Please input data in yyyymmdd format!')
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(curr_dir + '/cache.txt') as cache_file:
        for line in cache_file:
            feed_json = json.loads(line)
            feed_access_date = time.strptime(feed_json['access_time'], '%Y-%m-%d %H:%M:%S.%f')
            url = feed_json['feed_url']
            if feed_access_date > date_to_show and (not url_to_show or url == url_to_show):
                feed_json = json.dumps(feed_json, indent=2)
                print(json.loads(feed_json))


def parse_arguments(arguments):
    args_parser = argparse.ArgumentParser(prog='Stychnevsky RSS Reader',
                                          description='Reader to parse RSS and output news',
                                          epilog='RSS Reader 2020')

    args_parser.add_argument('url', nargs='?', action="store", help='url-address of feed to parse')
    args_parser.add_argument('--version', action="store_true", help='Print version info and exit program. '
                                                                    'Version changed after every program launch')
    args_parser.add_argument('--json', action="store_true", help='Print result as JSON')
    args_parser.add_argument('-v', '--verbose',  action="store_true",
                             help='Outputs verbose status messages')
    args_parser.add_argument('--limit', '-l', action="store",
                             type=int,
                             help='Limit news number if this parameter provided')
    args_parser.add_argument('--date', '-d', action="store",
                             help='Print all feeds from cache from appropriate date and appropriate source')
    args_parser.add_argument('--output-path', action="store", default=os.path.expanduser("~"),
                             help='In this argument you can set path to save epub and html files. '
                                  'Home directory is default')
    args_parser.add_argument('--to-epub', action="store_true",
                             help='Generate epub file with news. Use --output-path to select directory to save it')
    args_parser.add_argument('--to-html', action="store_true",
                             help='Generate html file, which include only. '
                                  'Use --output-path arg to select directory to save')

    return args_parser.parse_args(arguments)


def setup_logger():
    global log
    log = logging.getLogger('main_logger')
    log.setLevel(logging.INFO)
    global formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    fh = logging.FileHandler(curr_dir + '/logs.log')

    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    log.addHandler(fh)


def read_rss():
    cl_args = parse_arguments(sys.argv[1:])
    setup_logger()

    if cl_args.verbose:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        output_formatter = logging.Formatter('%(levelname)s - %(message)s')
        ch.setFormatter(output_formatter)
        log.addHandler(ch)

    log.info('Program started')

    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(curr_dir + '/version.txt', 'r+') as ver_file:
        prev_version = ver_file.readline()
        try:
            main_version, sub_version = prev_version.split('.')
        except ValueError:
            logging.error('Error during parsing version.txt. ValueError in spliting version data.')
            print("Version Error. Wrong Data in version.txt. Version has not been changed")
        else:
            new_version = main_version + '.' + str(int(sub_version) + 1)
            ver_file.seek(0)
            ver_file.write(new_version)
            if cl_args.version:
                print('Current version of program: ', prev_version)
                log.info('Program ended after Show Version mode')
                return

    if cl_args.date:
        display_cache(cl_args.url, cl_args.date)
        log.info('Program ended after Show Cache mode')
        return

    check_internet_connection()
    check_if_url_valid(cl_args.url)
    feed = Feed(cl_args.url, cl_args.limit)
    log.info('Feed object created')

    if feed.no_entries_in_feed:
        log.info('No entries in feed. Program ended')
        print('===\nSorry, page {link} does not contain any entries\n==='.format(link=cl_args.url))
        return

    if cl_args.json:
        feed.print_json()
        log.info('Feed object printed as JSON')
    else:
        feed.print()
        log.info('Feed object printed')

    if cl_args.to_epub:
        feed.create_epub(cl_args.output_path)
        log.info('epub file created')

    if cl_args.to_html:
        feed.create_html(cl_args.output_path)
        log.info('html file created')

    feed.caching()
    log.info('Program ended')


if __name__ == '__main__':
    read_rss()
