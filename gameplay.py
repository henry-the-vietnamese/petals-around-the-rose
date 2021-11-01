#!/usr/bin/env python3

#
# File:         gameplay.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  The CPU of the game (imported into the main.py file)
#               It works whether the user wins/loses and 
#               determines consecutive guesses.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


"""
The random module allows for the generation of
random numbers - face values on the dice.
Only one function - randint() - of this module is needed and
therefore only it is imported to 
increase code efficiency.

The predefined dice module displays the face value of dice to the screen.

In general, the random module gives the face of each die a value 
which is displayed to the screen using the dice module.
"""
from random import randint
import dice


def guess_validation():
    """Docstring for the function guess_validation().
    
    Validate guess from the user which should be an integer.

    Returns
    -------
    int
        The valid user guess for the game.
    """
    try:
        GUESS = int(input('Please enter your guess for the roll: '))
    except ValueError:
        print('Invalid value! The face value of a die is an integer data type.\n')
        GUESS = guess_validation()
    finally:
        return GUESS


def start_game(
        ROUND, CONSECUTIVE_CORRECT, 
        CONSECUTIVE_INCORRECT, FINAL_CORRECT, 
        FINAL_INCORRECT, consecutive):
    """Docstring for the function start_game()
    
    The CPU of the game. 
    It also calls the predefined called dice.py to 
    display the face values of the dice to the screen, 
    work out the answer to the game, 
    prompt the user for guesses and evaluate them,
    check for four consecutive guesses.
    
    Parameters
    ----------
    ROUND : int
        The number of games will be played.
    CONSECUTIVE_CORRECT : int
        The number of consecutive correct guesses.
    CONSECUTIVE_INCORRECT : int
        The number of consecutive incorrect guesses.
    FINAL_CORRECT : int
        The number of correct guesses in total.
    FINAL_INCORRECT : int
        The number of incorrect guesses in total.
    consecutive : list
        The list storing either 'correct' and 'incorrect'
        to keep track of consecutive 
        correct or incorrect guesses.

    Returns
    -------
    ROUND : int
        The number of games the user has played up to this point.
    CONSECUTIVE_CORRECT : int
        The number of consecutive correct guesses
        the user has received up to this point.
    CONSECUTIVE_INCORRECT : int
        The number of consecutive incorrect guesses
        the user has received up to this point.
    FINAL_CORRECT : int
        The number of correct guesses in total.
    FINAL_INCORRECT : int
        The number of incorrect guesses in total.
    consecutive :list
        The elements contained are either 'correct' or
        'incorrect' which will then be used to 
        compare whether correct or incorrect 
        guesses are consecutive.
        It might be empty if the correct or incorrect
        guesses are not consecutive.
    """
    # Start the game.
    ROUND += 1

    # Initialise an empty list to store 
    # five randomly generated dice rolls.
    dice_list = []
    for _ in range(5):
        dice_list.append(randint(1, 6))

    # Call the predefined function to display 
    # the randomly generated dice rolls to the screen.
    dice.display_dice(
        dice_list[0],
        dice_list[1],
        dice_list[2],
        dice_list[3],
        dice_list[4],
    )

    # Work out the answer.
    SCORE = 0               # Score starts with 0.
    for face_value in dice_list:
        if face_value == 3:
            SCORE += 2
        elif face_value == 5:
            SCORE += 4
        else:               # face_value = 1, 2, 4, 6
            SCORE += 0

    # Prompt for and read the user guess.
    # The called function will validate the guess.
    GUESS = guess_validation()

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
    if ('correct' in consecutive) and ('incorrect' in consecutive):
        # Reset variables to 0 and empty the list
        # when correct or incorrect guesses are not consecutive.
        CONSECUTIVE_CORRECT = 0
        CONSECUTIVE_INCORRECT = 0
        consecutive.clear()

    # Now the guesses are consecutive.
    if len(consecutive) == 4:
        if 'correct' in consecutive and 'incorrect' not in consecutive:
            print('\nCongratulations! You have worked out the secret!',
                  'Make sure you don\'t tell anyone!',
                  sep='\n',
            )
        elif ('incorrect' in consecutive) and ('correct' not in consecutive):
            print('Hint: The name of the game is important... Petals Around the Rose.')
        # Reset variables to 0 and empty the list 
        # after displaying messages about consecutive guesses.
        CONSECUTIVE_CORRECT = 0
        CONSECUTIVE_INCORRECT = 0
        consecutive.clear()

    # Returns. 
    return (
        ROUND, CONSECUTIVE_CORRECT, 
        CONSECUTIVE_INCORRECT, FINAL_CORRECT, 
        FINAL_INCORRECT, consecutive,
    )
