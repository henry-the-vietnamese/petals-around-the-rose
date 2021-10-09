#!/usr/bin/env python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  Build a mathematical challenging puzzle - Petals Around The Rose.
#               This is the main interface of the puzzle.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.

"""
The predefined game_body module consists of the GamePlay function which calls another predefined module to display the face values of the dice to the screen, works out the answer to the game, prompts for and evaluates user guesses, and checks for four consecutive guesses.
"""

from game_body import GamePlay


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

# Create 5 variables to keep track of the flow of the game.
ROUND = 0                   # The number of games will be played.
CONSECUTIVE_CORRECT = 0     # The number of consecutive correct guesses.
CONSECUTIVE_INCORRECT = 0   # The number of consecutive incorrect guesses.
FINAL_CORRECT = 0           # The number of correct guesses in total.
FINAL_INCORRECT = 0         # The number of incorrect guesses in total.

# Create an empty list to keep track of correct or incorrect guesses in a row.
consecutive = []

# Ask if the user wants to start the game.
start = input('\nWould you like to play Petals Around the Rose [y|n]? ')

while start.lower() not in ['y', 'yes', 'n', 'no']:
    print("Please enter either 'y' or 'n'.")
    start = input('\nWould you like to play Petals Around the Rose [y|n]? ')

while start.lower() in ['y', 'yes']:
    ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive = GamePlay(ROUND, CONSECUTIVE_CORRECT, CONSECUTIVE_INCORRECT, FINAL_CORRECT, FINAL_INCORRECT, consecutive)

    # Repeat the game.
    start = input('\nRoll dice again [y|n]? ')

    while start.lower() not in ['y', 'yes', 'n', 'no']:
        print("Please enter either 'y' or 'n'.")
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
