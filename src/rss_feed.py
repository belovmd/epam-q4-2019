import json
import unicodedata
from xml.dom import minidom

# Names of different rss formats
RSS_FOMRATS = ['rss', 'atom', 'unknown']
# Root rss feed tags
RSS_ROOT_TAG = ['channel', 'feed']
# Tags of rss entries
RSS_ENTRY_TAG = ['item', 'entry']
# Tags of rss summaries
RSS_SUMMARY_TAG = ['description', 'summary']
# Tags for timestamp of rss issue
RSS_UPDATED_TAG = ['pubDate', 'updated']
# Tag string for rss link
RSS_LINK_TAG = 'link'
# Tag string for rss title
RSS_TITLE_TAG = 'title'
# Current rss format ids
RSS_FOMRAT = 0
ATOM_FOMRAT = 1
UNKNOWN_FOMRAT = 2


class Rss_feed(object):
    """Represents rss feed"""

    def __init__(self, xml_string='', options=dict()):
        """Constructor"""

        self.options = options
        self.xml_string = xml_string
        self.parse_xml_string(xml_string)

    def parse_xml_string(self, xml_string):
        """Convert xml string to rss feed"""

        self.xml_string = xml_string
        self.entries = []
        self.rss_format_id = UNKNOWN_FOMRAT

        self.printv('> parsing rss_xml...')
        if not xml_string:
            return

        self.dom = minidom.parseString(xml_string)
        self.dom.normalize()
        self.rss_format_id = self.determine_rss_format(xml_string)

        self.printv(
            ">> format detected:",
            RSS_FOMRATS[self.rss_format_id])

        if self.rss_format_id == UNKNOWN_FOMRAT:
            self.printv(">>> format unknown, cannot parse")
            return

        self.entries = self.dom.getElementsByTagName(
            RSS_ENTRY_TAG[self.rss_format_id]
        )

        self.printv("> found {} entries".format(len(self.entries)))

    def printv(self, *a):
        """Print message if verbose mode is enabled"""

        if self.options and self.options.mode_verbose:
            print(' '.join(a))

    def determine_rss_format(self, xml_string):
        """Detect rss format from xml string"""

        if not self.dom:
            return UNKNOWN_FOMRAT
        if self.dom.getElementsByTagName(RSS_ROOT_TAG[RSS_FOMRAT]):
            return RSS_FOMRAT
        if self.dom.getElementsByTagName(RSS_ROOT_TAG[ATOM_FOMRAT]):
            return ATOM_FOMRAT
        return UNKNOWN_FOMRAT

    def extract_value_from_node(node, tag):
        """Safty extract value from tag of node

        Args:
            node: node to parse
            tag: tag to extract value from
        """

        try:
            return (node.getElementsByTagName(tag)[0]
                    .childNodes[0].nodeValue)
        except Exception as e:
            print(
                "{}: cannot extract tag '{}' from node {}"
                .format(e, tag, node))
            return None

    def extract_attr_from_node(node, tag, attr):
        """Extracts attribute from tag of node

        Args:
            node: node to process
            tag: name of tag to extract from
            attr: name of attribtue
        """

        try:
            return (
                node.getElementsByTagName(tag)[0]
                .getAttribute(attr))
        except Exception as e:
            print("{}: cannot extract attr '{}' from node {}".format(
                e, attr, node))
            return None

    def render_titles(self, count=3):
        """Render titles of rss feed"""

        self.printv("> showing lastest {} entry titles:".format(count))

        for entry in self.entries[:count]:
            print(" - {}".format(
                entry.getElementsByTagName('title')[0]
                .childNodes[0].nodeValue))

    def parse_entry(self, entry):
        """Parse rss entry to separated fields

        Args:
            entry: rss entry to split
        Returns:
            tuple, containg title, summary, link and timestamp
        """

        title = Rss_feed.extract_value_from_node(
            entry, RSS_TITLE_TAG)
        summary = Rss_feed.extract_value_from_node(
            entry, RSS_SUMMARY_TAG[self.rss_format_id])
        if self.rss_format_id == ATOM_FOMRAT:
            link = Rss_feed.extract_attr_from_node(
                entry, RSS_LINK_TAG, 'href')
        elif self.rss_format_id == RSS_FOMRAT:
            link = Rss_feed.extract_value_from_node(
                entry, RSS_LINK_TAG
            )
        timestamp = Rss_feed.extract_value_from_node(
            entry, RSS_UPDATED_TAG[self.rss_format_id])

        title = unicodedata.normalize("NFKD", title)
        summary = unicodedata.normalize("NFKD", summary)

        return (title, timestamp, link, summary)

    def format_entry(self, entry):
        """Extract fields of rss entry and do formatting

        Args:
            entry: rss entry to process
        Returns:
            formatted string contaning formatted rss entry
        """
        title, timestamp, link, summary = self.parse_entry(entry)
        return "Title: {}\n Date: {}\n Link: {}\n\n{}\n{}\n".format(
            title, timestamp, link, summary, '-' * 30
        )

    def render_entries(self):
        """Render rss entries in text form"""

        count = self.options.limit

        self.printv("> showing lastest {} entries:".format(count))

        if self.options and self.options.json_format:
            print(self.prepare_json(count))
        else:
            if self.options.titles:
                self.render_titles(count)
            else:
                for entry in self.entries[:count]:
                    print(self.format_entry(entry))

    def prepare_json(self, count=3):
        """Prepare json output of rss entries"""

        entries_list = []

        for entry in self.entries[:count]:
            entry_dict = dict()
            title, timestamp, link, summary = self.parse_entry(entry)
            entry_dict['title'] = title
            entry_dict['timestamp'] = timestamp
            entry_dict['link'] = link
            entry_dict['summary'] = summary

            entries_list.append(entry_dict)

        return json.dumps(
            entries_list, indent=4, ensure_ascii=False)
