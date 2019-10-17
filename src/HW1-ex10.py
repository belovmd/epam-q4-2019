from time import localtime

activities = {8: 'sleeping',
              9: 'sport',
              17: 'working',
              18: 'commuting',
              20: 'eating',
              23: 'reading'}

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print("Sorry, it's secret time")
