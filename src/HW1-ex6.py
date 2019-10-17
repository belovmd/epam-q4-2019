import re

for test_string in ['37529-1236532', '375-44-3496734', 'ILL-EGAL']:
    if re.match(r'^\d{5}-\d{7}$', test_string):
        print(test_string, 'is a valid Belarus phone number')
    else:
        print(test_string, 'rejected (invalid number)')
