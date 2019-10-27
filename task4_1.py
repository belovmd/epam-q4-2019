"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

for example,
input:
07:05:45PM

output:
19:05:45
"""

s = input()
if s[-2:] == "PM":
    s = "{:02d}{}".format((int(s[:2]) % 12 + 12) % 24, s[2:-2])
else:
    s = "{:02d}{}".format(int(s[:2]) % 12, s[2:-2])
print(s)
