import tools
import requests
from rss_feed import Rss_feed


def get_rss_xml(url):
    try:
        res = requests.get(url)
        result = res.text
        return result
    except Exception as ex:
        print("Cannot process request, {}".format(ex))


def main():
    """Entry point of program"""

    print('[rss parser]')

    options = tools.process_arguments()
    rss_feed_string = get_rss_xml(options.source)
    rss_feed = Rss_feed(rss_feed_string, options)
    rss_feed.render_entries()


main()
