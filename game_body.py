#!/usr/bin/env python3

#
# File:         game_body.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  The CPU of the game, working out whether the user wins/loses and determining consecutive guesses.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.

"""
The random module generates 'pseudo-random' numbers - face values on the dice.
The predefined dice module displays the face value of dice to the screen.
Generally, the random module gives the face of each die a value which is displayed to the screen using the dice module.
"""

import random
import dice


def GamePlay(ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive):
    """
    Function to act as the brain of the puzzle/game. It calls a predefined module called dice.py to display the face values of the dice to the screen, works out the answer to the game, prompts for and evaluates user guesses, checks for four consecutive guesses.
    This function takes six parameters which are responsible for keeping track of the flow of the game.
    Parameters: ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive.
    Returns: All of the six mentioned parameters are returned from the function so that the function can be reused if the user opts to replay the game.
    """

    # Start the game.
    ROUND += 1

    # Create an empty list to store 5 randomly generated dice rolls.
    dicelist = []
    for _ in range(5):
        dicelist.append(random.randint(1, 6))

    # Call the predefined function to display the randomly generated dice rolls to the screen.
    dice.display_dice(
            dicelist[0],
            dicelist[1],
            dicelist[2],
            dicelist[3],
            dicelist[4],
    )

    # Work out the answer.
    SCORE = 0
    for face_value in dicelist:
        if face_value == 3:
            SCORE += 2
        elif face_value == 5:
            SCORE += 4
        else:               # face_value = 2, 4, 6
            SCORE += 0

    # Prompt for and read the user's guess.
    GUESS = ValidGuess()

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
        # Reset variables to 0 when correct or incorrect guesses are not consecutive.
        CONSECUTIVE_CORRECT = 0
        CONSECUTIVE_INCORRECT = 0
        consecutive.clear()

    # Now the guesses are consecutive.
    if len(consecutive) == 4:
        if 'correct' in consecutive and 'incorrect' not in consecutive:
            print('\nCongratulations! You have worked out the secret!',
                  'Make sure you don\'t tell anyone!',
                  sep = '\n',
            )
        elif 'incorrect' in consecutive and 'correct' not in consecutive:
            print('Hint: The name of the game is important... Petals Around the Rose.')
        # Reset variables to 0 after displaying messages about consecutive guesses.
        CONSECUTIVE_CORRECT = 0
        CONSECUTIVE_INCORRECT = 0
        consecutive.clear()

    # A fruitful function.
    return ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive


def ValidGuess():
    """
    Function to validate the user guess. Creating this function allows the validation (using try/except/finally) to continuously repeats until a valid guess is made.
    This function tales no parameters, as well as no global variables.
    Returns: the finally valid guess is returned.
    """

    try:
        GUESS = int(input('Please enter your guess for the roll: '))
    except ValueError:
        print('Invalid value! The face value of a die is an integer data type.\n')
        GUESS = ValidGuess()
    finally:
        return GUESS
