#!/usr/bin/env python3

#
# File:         petals.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  Build a mathematical challenging puzzle - Petals Around The Rose.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.

import dice
import random


# Create an empty to store 5 randomly generated dice rolls.
dicelist = []
for _ in range(5):
    i = random.randint(1, 6)
    dicelist.append(i)

# Call a function to display the randomly generated dice rolls to the screen.
dice.display_dice(
        dicelist[0], 
        dicelist[1], 
        dicelist[2],
        dicelist[3],
        dicelist[4],
)

# Display the game introduction.
print(
"""
Petals Around the Rose
----------------------
The name of the game is 'Petals Around the Rose'. The name of the
game is important. The computer will roll five dice and ask you to
guess the score for the roll. The score will always be zero or an
even number. Your mission, should you choose to accept it, is to
work out how the computer calculates the score. If you succeed in
working out the secret and guess correctly four times in a row, you
become a Potentate of the Rose.
"""
)

# Work out the solution.
score = 0
for i in dicelist:
    if i == 3:
        score += 2
    elif i == 5:
        score += 4
    else:
        score += 0

# Prompt for and read the user's guess.
guess = int(input('Please enter your guess for the roll: '))

if guess == score:
    print('Well done! You guessed it!')
else:
    if guess % 2 == 0:
        print(f'No sorry, it\'s {score} not {guess}.')
    else:
        print(f'No sorry, it\'s {score} not {guess}. The score is always even.')

# Repeat the game.
repeat = input('\nRoll dice again [y|n]? ')

while repeat.lower() in ['y', 'yes']:
    # Create an empty to store 5 randomly generated dice rolls.
    dicelist = []
    for _ in range(5):
        i = random.randint(1, 6)
        dicelist.append(i)
    # Call a function to display the randomly generated dice rolls to the screen.
    dice.display_dice(
            dicelist[0], 
            dicelist[1], 
            dicelist[2],
            dicelist[3],
            dicelist[4],
    )
    # Work out the solution.
    score = 0
    for i in dicelist:
        if i == 3:
            score += 2
        elif i == 5:
            score += 4
        else:
            score += 0
    # Prompt for and read the user's guess.
    guess = int(input('Please enter your guess for the roll: '))
    if guess == score:
        print('Well done! You guessed it!')
    else:
        if guess % 2 == 0:
            print(f'No sorry, it\'s {score} not {guess}.')
        else:
            print(f'No sorry, it\'s {score} not {guess}. The score is always even.')
    # Repeat the game.
    repeat = input('\nRoll dice again [y|n]? ')

