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
The predefined gameplay.py module consists of the function start_game() 
which calls another predefined module dice.py to display the face
values of the dice to the screen, work out the answer to the game,
prompt for and evaluate the user's guess, and lastly determine if
the user has four correct guesses in a row.

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
## 1. The number of games that will be played.
round = 0
## 2. The number of consecutive correct guesses.
consecutive_correct = 0
## 3. The number of correct guesses in total.
total_correct = 0
## 4. Become True if the user guesses incorrectly.
incorrect_guess = False     
## 5. Become True if the user guesses correctly four times in a row.
four_correct_in_row = False
## 6. Become True if the user has at least four correct guesses in a row.
more_than_4_correct_in_row = False

# Ask if the user wants to start the game.
play = False

while not play:
    play = input(
                '\nWould you like to play Petals Around the Rose'
                ' [y|n]? '
    )
    # 'play' input validation, must be either 'yes' or 'no'.
    while play.lower() not in ['y', 'yes', 'n', 'no']:
        print("Please enter either 'y' or 'n'.")
        play = input(
                    '\nWould you like to play Petals Around the Rose'
                    '[y|n]? '
        )

    # Start the game if the user says 'yes'.
    while play.lower() not in ['n', 'no']:
        """
        New values are assigned to the same variables so that 
        the game can run again with numbers keeping to be counted.
        """
        (round, consecutive_correct,
         total_correct, incorrect_guess, 
         four_correct_in_row) = start_game(round, consecutive_correct, 
                                           total_correct, incorrect_guess,
                                           four_correct_in_row) 

        # Evaluate the guesses to display appropriate message.
        if not incorrect_guess: # If the user didn't guess incorrectly.
            if four_correct_in_row:
                """
                If the user has already guessed correctly four times in
                a row, and now another correct guess is made, mark this 
                event so that appropriate message can be displayed later.
                """
                more_than_4_correct_in_row = True
            
            # If the user has four or more correct guesses in a row.
            if consecutive_correct == 4 or more_than_4_correct_in_row:
                # Reset the variable before playing again.
                consecutive_correct = 0
                # Prompt the user for a response to replaying the game.
                play = input('\nDo you want to keep playing [y|n]? ')
                ## 'play' input validation, must be either 'yes' or 'no'.
                while play.lower() not in ['y', 'yes', 'n', 'no']:
                    print("Please enter either 'y' or 'n'.")
                    play = input('\nDo you want to keep playing [y|n]? ')
        else:                   # If the user guessed incorrectly.    
            """
            This else branch prevents the event that the user responds
            'no' to the prompting message from the previous if branch.
            """
            if play not in ['n', 'no']:
                # Prompt the user for a response to stopping the game.
                abort = False
                
                while not abort:
                    abort = input('\nDo you give up [y|n]? ')
                
                    # 'abort' input validation, must be either yes or no.
                    while abort.lower() not in ['y', 'yes', 'n', 'no']:
                        print("Please enter either 'y' or 'n'.")
                        abort = input('\nDo you give up [y|n]? ')
                    
                    """
                    Now, depending on whether the user wants to give up, 
                    change the start variable so that the loop can continue.
                    """
                    if abort.lower() not in ['n', 'no']:
                        play = 'n'
                    else:
                        play = 'y'
                        # Reset the variable before playing again.
                        incorrect_guess = False

# Game summary.
if round:
    print(
    f"""\n
Game Summary
------------
You played {round} games:
 * Correct guesses:     {total_correct}
 * Incorrect guesses:   {round - total_correct}
    """
    )
    if more_than_4_correct_in_row:
        print('Congratulations, you are now a Potentate of the Rose.')
    else:
        print('Maybe you will work it out next time.')
    print('Thanks for playing!')
else:
    print('\nPlease play soon... :)')
