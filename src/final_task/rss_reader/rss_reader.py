import argparse
import cache_db
import datetime
from dateutil.parser import parse
import ebooker
import errors
import json
import logging
import logging.config
import requests
import sys
import utils
import xml.etree.ElementTree as ET


def version():
    """Dump RSS Reader version"""
    __version = "v0.4.0"
    version_logger = logging.getLogger("version_logger")

    version_logger.debug("RSS Reader version {}".format(__version))
    return __version


def create_parser():
    """Parse arguments from CLI interface."""
    parser = argparse.ArgumentParser(
        description="Pure Python command-line RSS reader."
    )
    parser.add_argument("source", type=str, help="RSS URL")
    parser.add_argument(
        "--version", help="Print version info", action="store_true"
    )
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--verbose",
        help="Outputs verbose status messages",
        action="store_true",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit news topics if this parameter required",
    )
    parser.add_argument("--date", type=str, help="Day in %Y%m%d format")
    parser.add_argument(
        "--output-path",
        type=str,
        help="Format converter output, defaults to home dir",
    )
    parser.add_argument(
        "--to-fb2", action="store_true", help="Convert RSS to fb2 format"
    )
    parser.add_argument(
        "--to-epub", action="store_true", help="Convert RSS to epub format"
    )

    return parser


def fetch_rss(link):
    """Fetch text from URL."""
    fetch_rss_logger = logging.getLogger("fetch_rss_logger")
    try:
        fetch_rss_logger.debug("Fetchin link {}".format(link))
        r = requests.get(link)
        # Enable to check downloaded file format
        #        fetch_rss_logger.debug("Fetched: \n {}".format(r.text))
        return r.text
    except Exception:
        fetch_error = errors.FetchRssError(
            "Network error fetchig source, is {} alive?".format(link)
        )
        fetch_rss_logger.error(fetch_error)
        raise fetch_error


def parse_xml(xml, limit=None):
    """Parse rss xml into """

    def parse_newsitem(item):
        """Parses newsitems from ElementTree"""
        parse_newsitem_logger = logging.getLogger("parse_newsitem_logger")
        temp_item = {}
        temp_item["Title"] = utils.dehtml(item.find("title").text)
        temp_item["Date"] = parse(item.find("pubDate").text)
        temp_item["Link"] = item.find("link").text
        temp_item["Description"] = utils.dehtml(item.find("description").text)
        temp_item["HTML_desc"] = item.find("description").text
        parse_newsitem_logger.debug("Got item:\n {}".format(temp_item))
        return temp_item

    parse_xml_logger = logging.getLogger("parse_xml_logger")
    rss = ET.fromstring(xml)
    # Enable to check downloaded file format
    #    parse_xml_logger.debug("Digesting rss xml:\n {}".format(xml))
    results_channel = rss.find("channel").find("title").text
    parse_xml_logger.debug("Channel Title: {}".format(results_channel))
    results_items = []
    if limit and limit > 0:
        parse_xml_logger.debug("Items to process: {}".format(limit))
        for item in rss.iter(tag="item"):
            results_items.append(parse_newsitem(item))
            limit -= 1
            if limit < 1:
                break
        parse_xml_logger.debug("Items to process: {}".format(limit))
    else:
        for item in rss.iter(tag="item"):
            results_items.append(parse_newsitem(item))
    # Enable to check output data
    #    parse_xml_logger.debug("Digested rss:\n {}".format(results_items))
    return results_channel, results_items


def print_output(data):
    printer_logger = logging.getLogger("printer_logger")
    printer_logger.debug("Printing output.")
    # Enable to check printing data
    #    printer_logger.debug("Printing data:\n {}".format(data))
    title, items = data
    print(title)
    for item in items:
        for k, v in item.items():
            if k == "HTML_desc":
                pass
            elif isinstance(v, datetime.datetime):
                print(k, ":", v.isoformat())
            else:
                print(k, ":", v)
        print()


def dump_output(data):
    dump_logger = logging.getLogger("dump_logger")
    dump_logger.debug("Dumping data to dump.json")
    # Enable to check printing data
    #    dump_logger.debug("Dumping data:\n {}".format(data))
    with open("dump.json", "w") as f:
        json.dump(data, f, default=str)


def main():
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.version:
        print(version())
        quit()

    if args.date:
        conn = cache_db.create_connection()
        with conn:
            for i in cache_db.show_db(conn, args.date):
                for j in i:
                    print(j)
            quit()

    if args.to_fb2 or args.to_epub:
        ebooker.prepare_dirs("HTML_Out")

    raw = fetch_rss(args.source)

    if args.limit:
        processed = parse_xml(raw, args.limit)
    else:
        processed = parse_xml(raw)
    print_output(processed)

    title, items = processed
    conn = cache_db.create_connection()
    with conn:
        cache_db.create_news_table(conn)
        for item in items:
            cache_db.create_newsitem(conn, title, item)

    if args.to_fb2 or args.to_epub:
        out_file_path = "output"
        for item in items:
            ebooker.cook_html(title, args.source, item)
        if args.output_path:
            out_file_path = args.output_path
        if args.to_fb2:
            out_file_path += ".fb2"
            ebooker.convert(out_file_path, "fb2")
        elif args.to_epub:
            out_file_path += ".epub"
            ebooker.convert(out_file_path, "epub")

    if args.json:
        dump_output(processed)


if __name__ == "__main__":
    main_inner_logger = logging.getLogger("main_inner_logger")
    try:
        main_inner_logger.debug("Starting rss_reader inner main func")
        main()
    except Exception as e:
        main_inner_logger.error(e)
        print(
            errors.RssReaderCriticalError(
                "Fatal error. Pass --verbose to debug."
            )
        )
