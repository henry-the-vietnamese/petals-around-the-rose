#!/usr/bin/env python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  Build a mathematical challenging puzzle/game -
#               Petals Around The Rose.
#               This is the main interface of the game.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


"""
The predefined gameplay module consists of the function start_game() 
which calls another predefined module to display the face values of 
the dice to the screen, work out the answer to the game, prompt for 
and evaluate user guesses, and check for four consecutive guesses.

The module comprises two functions in total, but only one is imported 
as the other one is not called in this file and thus not imported to
increase code efficiency.
"""
from gameplay import start_game


# Display the game's introduction.
print(
"""
Petals Around the Rose
----------------------
The name of the game is 'Petals Around the Rose'. The name of the
game is important. The computer will roll dice and ask you to guess
the score for the roll. The score will always be zero or an even
number. Your mission, should you choose to accept it, is to work out
how the computer calculates the score. If you succeed in working
out the secret and guess correctly four times in a row, you become a
Potentate of the Rose.
"""
)

# Variable initialisation.
## 1. The number of games will be played.
ROUND = 0
## 2. The number of consecutive correct guesses.
CONSECUTIVE_CORRECT = 0
## 3. The number of correct guesses in total.
TOTAL_CORRECT = 0
## 4. Become True if the user guesses incorrectly.
incorrect_guess = False     
## 5. Become True if the user guesses correctly four times in a row.
potentate = False
## 6. Become True if the user has at least four correct guesses in a row.
more_than_4_correct_in_row = False

# Ask if the user wants to start the game.
play = None

## A response other than 'yes' means the game will not be played.
while play not in ['n', 'no', 'n'.upper(), 'no'.upper()]:
    """
    The string.upper() method is applied to the items instead of the
    'play' variable as it is a 'NoneType' object having no attribute 'lower'.
    """
    play = input(
                '\nWould you like to play Petals Around the Rose'
                ' [y|n]? '
           )
    ## 'play' input validation, must be either 'yes' or 'no'.
    while play.lower() not in ['y', 'yes', 'n', 'no']:
        print("Please enter either 'y' or 'n'.")
        play = input(
                    '\nWould you like to play Petals Around the Rose'
                    '[y|n]? '
               )

    # Start the game if the user says 'yes'.
    while play.lower() in ['y', 'yes']:
        """
        New values are assigned to the same variables so that 
        the game can run again with numbers keeping to be counted.
        """
        (ROUND, CONSECUTIVE_CORRECT,
         TOTAL_CORRECT, incorrect_guess, 
         potentate) = start_game(ROUND, CONSECUTIVE_CORRECT, 
                                 incorrect_guess, TOTAL_CORRECT, 
                                 potentate) 

        # Ask if the user wants to play the game again.
        if potentate:
            more_than_4_correct_in_row = True

        # If the user didn't guess incorrectly.
        if not incorrect_guess:
            # If the user has four or more correct guesses in a row.
            if CONSECUTIVE_CORRECT == 4 or more_than_4_correct_in_row:
                # Reset the variable before playing again.
                CONSECUTIVE_CORRECT = 0
                # Prompt the user for a response to replaying the game.
                play = input('\nDo you want to keep playing [y|n]? ')
                ## 'play' input validation, must be either 'yes' or 'no'.
                while play.lower() not in ['y', 'yes', 'n', 'no']:
                    print("Please enter either 'y' or 'n'.")
                    play = input('\nDo you want to keep playing [y|n]? ')
            
        else:
            if play in ['y', 'yes']:
                # Prompt the user for a response to stopping the game.
                abort = input('\nDo you give up [y|n]? ')
                ## 'abort' input validation, must be either yes or no.
                while abort.lower() not in ['y', 'yes', 'n', 'no']:
                    print("Please enter either 'y' or 'n'.")
                    abort = input('\nDo you give up [y|n]? ')

                # Depend on whether the user wants to give up, 
                # change the start variable.
                if abort.lower() in ['y', 'yes']:
                    play = 'n'
                elif abort.lower() in ['n', 'no']:
                    play = 'y'
                    # Reset the variable before playing again.
                    incorrect_guess = False

# Game summary.
if ROUND != 0:
    print(
    f"""\n
Game Summary
------------
You played {ROUND} games:
 * Correct guesses:     {TOTAL_CORRECT}
 * Incorrect guesses:   {ROUND - TOTAL_CORRECT}
    """
    )
    if not incorrect_guess and more_than_4_correct_in_row:
        print('Congratulations, you are now a Potentate of the Rose.')
    else:
        print('Maybe you will work it out next time.')
    print('Thanks for playing!')
else:
    print('\nPlease play soon... :)')
