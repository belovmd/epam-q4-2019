#!/usr/bin/env python3.7

"""Time, conditionals, from..import, for..else .

10 lines: Time, conditionals, from..import, for..else
from https://wiki.python.org/moin/SimplePrograms .

"""

from time import localtime

ACTIVITIES = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting'}

TIME_NOW = localtime()
HOUR = TIME_NOW.tm_hour

for activity_time in sorted(ACTIVITIES.keys()):
    if HOUR < activity_time:
        print(ACTIVITIES[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')
