"""Arguments from command-line are parsed in this module."""

import argparse
import logging
import news_functions
import sys


def main(args):
    """Convert derived arguments to dict and passes it to function for

    defining further actions of the program.
    """
    parser = argparse.ArgumentParser(description='''Pure Python command-line
                                                    RSS reader.''')
    parser.add_argument('source', help='RRS URL')
    parser.add_argument('--version', help='Print version info', action='count')
    parser.add_argument('--json', dest='json_',
                        help='Print result as JSON in stdout', action='count')
    parser.add_argument('--verbose', help='Outputs verbose status messages',
                        action='count')
    parser.add_argument('--limit', type=int, help='''Limit news topics if this
                                                     parameter provided''')
    parser.add_argument('--date', help="Print date's news")
    parser.add_argument('--to-fb2', dest='to_fb2', help='''Generate .fb2 file
                        with news''', action='count')
    parser.add_argument('--to-epub', dest='to_epub', help='''Generate .epub
                        file with news''', action='count')
    parser.add_argument('--output-path', dest='path', help='Path to new file')
    parser.add_argument('--colorize', action='count', help='''Print the result
                        of the utility in colorized mode''')
    my_namespace = parser.parse_args(args)
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    args_dict = vars(my_namespace)
    news_functions.choose_action(**args_dict)


if __name__ == "__main__":
    main(sys.argv[1:])
