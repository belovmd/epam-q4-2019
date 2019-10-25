#!/usr/bin/env python3.7

"""Guess the Number".

33 lines: "Guess the Number" Game (edited)
from http://inventwithpython.com.

"""

import random

guesses_made = 0

NAME = input('Hello! What is your name?\n')

NUMBER = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(NAME))

while guesses_made < 6:

    guess = int(input('Take a guess: '))

    guesses_made += 1

    if guess < NUMBER:
        print('Your guess is too low.')

    if guess > NUMBER:
        print('Your guess is too high.')

    if guess == NUMBER:
        break

if guess == NUMBER:
    print('Good job, {0}! You guessed my number in {1}guesses!'
          .format(NAME, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(NUMBER))
