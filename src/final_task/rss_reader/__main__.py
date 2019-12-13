import rss_reader.rss_reader as rr
import sys


def main(args=None):
    """Entry points for setuptools"""

    if args is None:
        args = sys.argv[1:]
    try:
        rr.main()
    except Exception:
        print(
            rr.errors.RssReaderCriticalError(
                "Fatal error. Pass --verbose to debug."
            )
        )


if __name__ == "__main__":
    main()
