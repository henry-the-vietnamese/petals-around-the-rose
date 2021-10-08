#!/usr/bin/env python3

#
# File:         petals.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  The CPU of the game, working out whether the user wins/loses.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.

import dice
import random


def GamePlay(ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive):
    # Start the game.
    ROUND += 1

    # Create an empty list to store 5 randomly generated dice rolls.
    dicelist = []
    for _ in range(5):
        i = random.randint(1, 6)
        dicelist.append(i)

    # Call the predefined function to display the randomly generated dice rolls to the screen.
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
        else:               # i = 2, 4, 6
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

    # A fruitful function.
    return ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive


