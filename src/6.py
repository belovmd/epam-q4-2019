import re
for test_string in ["555-1212", "144-2342", "23423422", "Something"]:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is valid US local phone number')
    else:
        print(test_string, 'rejected')
