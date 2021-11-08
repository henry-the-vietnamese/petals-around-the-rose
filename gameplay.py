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
The random module allows for the generation of random numbers 
(face values of the dice).
Only one function - randint() - of this module is needed and 
therefore only one is imported to increase code efficiency.

The predefined dice module displays the face value of dice 
to the screen.

In general, the random module gives the face of each die 
a value which is displayed to the screen using the dice module.
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
    # try...except...finally statement is used to prevent the program 
    # from crashing in case the user inputs a non-int value.
    try:
        GUESS = int(input('Please enter your guess for the roll: '))
    except ValueError:
        print(
            'Invalid value! '
            'The face value of a die is an integer data type.\n'
        )
        GUESS = guess_validation()
    finally:
        return GUESS


def start_game(
        ROUND, CONSECUTIVE_CORRECT, 
        incorrect_guess, TOTAL_CORRECT, 
        POTENTATE,
        more_4_in_row, consecutive):
    """Docstring for the function start_game()
    
    The CPU or the brain of the game. 
    The function also calls the predefined called dice.py to 
    display the face values of the dice to the screen, 
    work out the answer to the game, prompt the user for guesses 
    and evaluate them, check for four consecutive guesses.
    
    Parameters
    ----------
    ROUND : int
        The number of games will be played.
    CONSECUTIVE_CORRECT : int
        The number of consecutive correct guesses.
    incorrect_guess : int
        The number of consecutive incorrect guesses.
    TOTAL_CORRECT : int
        The number of correct guesses in total.
    POTENTATE : bool
        Become true when the user has guessed four or more 
        correctly in-a-row.
    consecutive : list
        The list storing either 'correct' and 'incorrect' to 
        keep track of consecutive correct or incorrect guesses.

    Returns
    -------
    ROUND : int
        The number of games the user has played up to this point.
    CONSECUTIVE_CORRECT : int
        The number of consecutive correct guesses
        the user has received up to this point.
    incorrect_guess : int
        The number of consecutive incorrect guesses
        the user has received up to this point.
    TOTAL_CORRECT : int
        The number of correct guesses in total.
    POTENTATE : bool
        Mark whether the user has guessed four or more correctly in-a-row.
    consecutive : list
        The items contained are either 'correct' or 'incorrect' 
        which will then be used to compare whether correct 
        or incorrect guesses are consecutive.
        It might be empty if the correct or incorrect guesses 
        are not consecutive.
    """
    # Start the game.
    ROUND += 1

    # Initialise an empty list to store five randomly generated dice rolls.
    diceList = []
    for _ in range(6):
        diceList.append(randint(1, 6))

    # Call the predefined function to display the randomly generated 
    # dice rolls to the screen.
    dice.display_dice(diceList)

    # Evaluate user's score. 
    SCORE = 0                   # Score starts with 0.
    for face_value in diceList:
        if face_value == 3:
            SCORE += 2
        elif face_value == 5:
            SCORE += 4
        else:                   # face_value = 1, 2, 4, 6
            SCORE += 0

    # Prompt for and read the user guess.
    # A predefined function will be called to validate the guess.
    GUESS = guess_validation()

    if GUESS == SCORE:
        CONSECUTIVE_CORRECT += 1
        TOTAL_CORRECT += 1
        # If the guesses are 4 in a row.
        if CONSECUTIVE_CORRECT == 4:
            # The user has exactly 4 consecutive correct guesses.
            print(
                'Congratulations! You have worked out the secret!\n'
                'Make sure you don\'t tell anyone!'
            )

            if POTENTATE:
                more_4_in_row = True

            POTENTATE = True
        
        elif CONSECUTIVE_CORRECT > 0:
            print('Well done! You guessed it!')

    else:
        incorrect_guess = True
        if GUESS % 2 == 0:
            print(f'No sorry, it\'s {SCORE} not {GUESS}.')
        else:
            print(
                f'No sorry, it\'s {SCORE} not {GUESS}. ' 
                f'The score is always even.'
            )
        
        print(
            '\nHint: The name of the game is important... '
            'Petals Around the Rose.'
        )

    # Returns. 
    return (
        ROUND, CONSECUTIVE_CORRECT, 
        incorrect_guess, TOTAL_CORRECT, 
        POTENTATE,
        more_4_in_row, consecutive,
    )
