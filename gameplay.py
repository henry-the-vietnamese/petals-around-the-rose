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


def validateGuess():
    """Docstring for the function validateGuess().
    
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
        GUESS = validateGuess()
    finally:
        return GUESS


def start_game(
        rounds, consecutive_correct, 
        total_correct, incorrect_guess, 
        four_correct_in_row):
    """Docstring for the function start_game().
    
    The CPU or the brain of the game. 
    The function also calls the predefined called dice.py to 
    display the face values of the dice to the screen, 
    work out the answer to the game, prompt the user for guesses 
    and evaluate them, check for four consecutive guesses.
    
    Parameters
    ----------
    rounds : int
        The number of games will be played.
    consecutive_correct : int
        The number of consecutive correct guesses.
    total_correct : int
        The number of correct guesses in total.
    incorrect_guess : bool
        Become True if the user guesses incorrectly.
    four_correct_in_row : bool
        Become True if the user guesses correctly four times in a row.

    Returns
    -------
    rounds : int
        The number of games the user has played up to this point.
    consecutive_correct : int
        The number of consecutive correct guesses
        the user has received up to this point.
    total_correct : int
        The number of correct guesses in total.
    incorrect_guess : bool
        Mark whether the user has just entered an incorrect guess.
    four_correct_in_row : bool
        Mark whether the user has guessed correctly four times in a row.
    """
    # Start the game.
    rounds += 1

    # Initialise an empty list to store five generated dice rolls.
    diceList = []
    ## Start randomly rolling dice and store in the list.
    for _ in range(6):
        diceList.append(randint(1, 6))

    # Call the predefined function to display the generated dice rolls.
    dice.display_dice(diceList)

    # Calculate the result. 
    result = 0                   # Result starts at 0.
    for face_value in diceList:
        if face_value == 3:
            result += 2
        elif face_value == 5:
            result += 4
        else:                   # face_value = 1, 2, 4, 6.
            result += 0

    # Prompt for, read, and validate guess from the user.
    guess = validateGuess()

    # Compare the user's guess with the result.
    if guess == result:
        consecutive_correct += 1
        total_correct += 1
        # If the user has exactly four consecutive correct guesses.
        if consecutive_correct == 4:
            print(
                'Congratulations! You have worked out the secret!\n'
                'Make sure you don\'t tell anyone!'
            )

            # 'four_correct_in_row' variable becomes True to mark this event.
            four_correct_in_row = True
        # If the user simply has a correct guess, not four in a row.
        elif consecutive_correct > 0:
            print('Well done! You guessed it!')

    else:
        # 'incorrect_guess' variable becomes True to mark this event.
        incorrect_guess = True
        """
        Determine whether the incorrect guess is even or not to
        display an appropriate message.
        """
        if guess % 2 == 0:
            print(f'No sorry, it\'s {result} not {guess}.')
        else:
            print(
                f'No sorry, it\'s {result} not {guess}. ' 
                f'The score is always even.'
            )
        print(
            '\nHint: The name of the game is important... '
            'Petals Around the Rose.'
        )

    # Return values for global usage. 
    return (rounds, consecutive_correct, 
            total_correct, incorrect_guess,
            four_correct_in_row)
