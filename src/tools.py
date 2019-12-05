import argparse

# Default limit of rendered rss issues
Default_limit = 3
# Version of rss reader
Program_version = 'v0.03'
# Description of the program
Program_descirption = 'Really simple rss parser'


def process_arguments():
    """Process program arguments"""

    aparser = argparse.ArgumentParser(
        description=Program_descirption, add_help=True)

    aparser.add_argument(
        '--version', action='store_true',
        dest='show_version', help='Print version info')
    aparser.add_argument(
        '--verbose', action='store_true', default=False,
        dest='mode_verbose', help='Outputs verbose status messages')
    aparser.add_argument(
        '--limit', action='store', default=Default_limit, type=int,
        help='Limit news topics to given value, default={}'
        .format(str(Default_limit))
    )
    aparser.add_argument(
        'source', action='store')
    aparser.add_argument(
        '--json', action='store_true', default=False,
        dest='json_format', help="Output entries in json format")
    aparser.add_argument(
        '--titles', action='store_true', default=False,
        help='render only titles or rss entries')

    args = aparser.parse_args()

    if args.show_version:
        print('\t{}, {}'.format(Program_descirption, Program_version))
        exit()

    if args.mode_verbose:
        print(args)

    return args
