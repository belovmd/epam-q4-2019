# script 1
print('Hello, world!')

# script 2
user_name = input('What is your name?\n')
print('Welcome to my world, %s.' % user_name)

# script 3
friend = ['Misha', 'Alex', 'Max', 'Feodor']
for i, name in enumerate(friend):
    print("My frend # {iteration} is {name}".format(iteration=i, name=name))

print("And you will be my frend # %s, %s" % (i + 1, user_name))
