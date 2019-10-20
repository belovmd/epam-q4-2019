from itertools import groupby
lines = '''
This is the
first paragraph.

This is the second.
something.


This is third.
something else again.
bla-bla-bla.
'''.splitlines()

for has_chars, frags in groupby(lines, bool):
    if has_chars:
        print(' '.join(frags))
