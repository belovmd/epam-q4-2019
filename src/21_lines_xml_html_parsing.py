#!/usr/bin/env python3.7

"""Example of work with XML/HTML.

21 lines: XML/HTML parsing from https://wiki.python.org/moin/SimplePrograms .

"""

# From http://effbot.org/zone/element-index.htm
import xml.etree.ElementTree as etree

DINNER_RECIPE = '''<html><body><table>
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>'''


TREE = etree.fromstring(DINNER_RECIPE)

# For invalid HTML use http://effbot.org/zone/element-soup.htm
# import ElementSoup, StringIO
# TREE = ElementSoup.parse(StringIO.StringIO(DINNER_RECIPE))

PANTRY = set(['olive oil', 'pesto'])
for ingredient in TREE.getiterator('tr'):
    amt, unit, item = ingredient
    if item.tag == "td" and item.text not in PANTRY:
        print("%s: %s %s" % (item.text, amt.text, unit.text))
