"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

for example,
input:
07:05:45PM

output:
19:05:45
"""

s = input()
hours = int(s[:2]) % 12
if s[-2:] == "PM":
    hours += 12

print("{:02d}{}".format(hours, s[2:-2]))
