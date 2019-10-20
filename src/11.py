REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''

Last_One = """
Last bottle of beer on the wall,
Last bottle of beer,
take it down, and go to bed,
There is no beer left!
"""

bottles_of_beer = 9

while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer,
                     bottles_of_beer - 1))
    bottles_of_beer -= 1

print(Last_One)
