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

# Create 5 variables to keep track of how many games will be played.
ROUND = 0
CONSECUTIVE_CORRECT = 0
CONSECUTIVE_INCORRECT = 0
FINAL_CORRECT = 0
FINAL_INCORRECT = 0

# Create a list to keep track of correct or incorrect guesses in a row.
consecutive = []

# Ask if the user wants to start playing.
start = input('\nWould you like to play Petals Around the Rose [y|n]? ')

while start.lower() not in ['y', 'yes', 'n', 'no']:
    print("Please enter either 'y' or 'n'.")
    start = input('\nWould you like to play Petals Around the Rose [y|n]? ')

while start.lower() in ['y', 'yes']:
    # Start the game.
    ROUND += 1

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
    SCORE = 0
    for i in dicelist:
        if i == 3:
            SCORE += 2
        elif i == 5:
            SCORE += 4
        else:
            SCORE += 0

    # Prompt for and read the user's guess.
    GUESS = int(input('Please enter your guess for the roll: '))

    if GUESS == SCORE:
        CONSECUTIVE_CORRECT += 1
        FINAL_CORRECT += 1
        consecutive.append('correct')
        print('Well done! You guessed it!')
    else:
        CONSECUTIVE_INCORRECT += 1
        FINAL_INCORRECT += 1
        consecutive.append('incorrect')
        if GUESS % 2 == 0:
            print(f'No sorry, it\'s {SCORE} not {GUESS}.')
        else:
            print(f'No sorry, it\'s {SCORE} not {GUESS}. The score is always even.')

    # Repeat the game.
    start = input('\nRoll dice again [y|n]? ')

    while start.lower() not in ['y', 'yes', 'n', 'no']:
        print("Please enter either 'y' or 'n'.")
        start = input('\nRoll dice again [y|n]? ')

    while start.lower() in ['y', 'yes']:
        # The game starts over.
        ROUND += 1
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
        SCORE = 0
        for i in dicelist:
            if i == 3:
                SCORE += 2
            elif i == 5:
                SCORE += 4
            else:
                SCORE += 0
        # Prompt for and read the user's guess.
        GUESS = int(input('Please enter your guess for the roll: '))
        if GUESS == SCORE:
            CONSECUTIVE_CORRECT += 1
            FINAL_CORRECT += 1
            consecutive.append('correct')
            print('Well done! You guessed it!')
        else:
            CONSECUTIVE_INCORRECT += 1
            FINAL_INCORRECT += 1
            consecutive.append('incorrect')
            if GUESS % 2 == 0:
                print(f'No sorry, it\'s {SCORE} not {GUESS}.')
            else:
                print(f'No sorry, it\'s {SCORE} not {GUESS}. The score is always even.')
        # Check for four consecutive guesses.
        if ['correct', 'incorrect'] in consecutive:
            # Reset to 0 if correct or incorrect guesses are not consecutive.
            CONSECUTIVE_CORRECT = 0
            CONSECUTIVE_INCORRECT = 0
            consecutive.clear()
        # Now the guesses are consecutive.
        if len(consecutive) == 4:
            if 'correct' in consecutive and 'incorrect' not in consecutive:
                print('Congratulations! You have worked out the secret!',
                      'Make sure you don\'t tell anyone!',
                      sep = '\n',
                )
            elif 'incorrect' in consecutive and 'correct' not in consecutive:
                print('Hint: The name of the game is important... Petals Around the Rose.')
            CONSECUTIVE_CORRECT = 0
            CONSECUTIVE_INCORRECT = 0
            consecutive.clear()
        # Repeat the game.
        start = input('\nRoll dice again [y|n]? ')

# Game summary.
if ROUND !=  0:
    print(
    f"""

    Game Summary
    ============

    You played {ROUND} games:
      |--> Number of correct guesses: {FINAL_CORRECT}
      |--> Number of incorrect guesses: {FINAL_INCORRECT}

    Thanks for playing!
    """
    )
else:
    print('\nNo worries... another time perhaps... :)')
