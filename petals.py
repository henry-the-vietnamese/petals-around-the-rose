#!/usr/bin/env python3

#
# File:         petals.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  Build a mathematical challenging puzzle/game -
#               Petals Around the Rose.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


# --------------------------- Module Imports -------------------------- #
"""
The random module allows for the generation of random numbers 
(face values of the dice).
The predefined dice module displays the face value of dice 
to the screen.
In general, the random module gives the face of each die 
a value which is displayed to the screen using the dice module.
"""
import random
import dice


# ------------------------ Function Definitions ----------------------- #
def validate_guess():
    """Docstring for the function validate_guess().
    
    Prompt for, read, and validate a guess from the user which should 
    be a positive integer.

    Returns
    -------
    int
        The positive integer guess received from the user.
    """
    guess = None
    
    while guess is None or guess < 0:
        try:
            guess = float(input('Please enter your guess for the roll: '))
            if guess < 0:
                print('Error: negative number\n')
        except ValueError as e:
            print('Error:', e, '\n')
    
    return int(guess)


def calculate_petals(diceList):
    """Docstring for the function calculate_petals().

    Calculate the number of petals around the rose in the current round.

    Parameters
    ----------
    diceList : list
        The list whose items are the face values of the dice.

    Returns
    -------
    int
        The number of petals around the rose / The result of this round.
    """
    result = 0 
    for face_value in diceList:
        if face_value == 3:
            result += 2
        elif face_value == 5:
            result += 4
        else:                   # face_value = 1, 2, 4, 6
            result += 0
    return result


def ask_to_play(rounds, guess_correctly):
    """Docstring for the function ask_to_play().

    Ask if the user wants to play the game again.

    Parameters
    ----------
    rounds : int
        The number of rounds the user has played.
        The value 0 (False) for not having played any game.
    guess_correctly : int
        The number of correct guesses in a row. 
        The value 0 (Flase) means an incorrect guess is just made.

    Returns
    -------
    str
        The user's response if they want to play again. 
    """
    EXPECTED_INPUT = ['y', 'yes', 'n', 'no']
    valid = False

    if not rounds:
        # Ask if they want to start the game.
        while not valid:
            play = input('\nWould you like to play Petals Around the Rose [y|n]? ')
            if play.lower() not in EXPECTED_INPUT:
                print("Please enter either 'y' or 'n'.")
            else:
                valid = True
    
    else:
        if guess_correctly:
            # Just guessed correctly, ask if they want to replay the game.
            while not valid:
                play = input('\nDo you want to keep playing [y|n]? ')
                if play.lower() not in EXPECTED_INPUT:
                    print("Please enter either 'y' or 'n'.")
                else:
                    valid = True

        else:
            # Just guessed incorrectly, ask if they want to stop the game.
            while not valid:
                stop = input('\nDo you give up [y|n]? ')
                if stop.lower() not in EXPECTED_INPUT:
                    print("Please enter either 'y' or 'n'.")
                else:
                    valid = True

            if stop.lower() not in EXPECTED_INPUT[2:4]:
                play = 'n'
            else:
                play = 'y'

    return play


# ------------------------------ Program ------------------------------ #
print(
    f'File:         petals.py',
    f'Author:       Tan Duc Mai',
    f'Email:        tan.duc.work@gmail.com',
    f'Description:  Build a mathematical challenging puzzle/game -',
    f'              Petals Around the Rose.',
    f'I hereby declare that I completed this work without any improper help',
    f'from a third party and without using any aids other than those cited.',
    sep='\n',
    end='\n\n',
)

# Display the game's instructions.
print(
    'Petals Around the Rose',
    '----------------------',
    'The name of the game is \'Petals Around the Rose\'. The name of the',
    'game is important. The computer will roll dice and ask you to guess',
    'the score for the roll. The score will always be zero or an even',
    'number. Your mission, should you choose to accept it, is to work out',
    'how the computer calculates the score. If you succeed in working',
    'out the secret and guess correctly four times in a row, you become a',
    'Potentate of the Rose.',
    sep='\n',
    end='\n\n',
)

# Variable initialisation.
rounds = 0                  # The number of games that will be played.
consecutive_correct = 0     # The number of consecutive correct guesses.
total_correct = 0           # The number of correct guesses in total.
potentate = False           # Become True if the user guessed correctly 
                                # four times in a row.

# Ask if the user wants to start playing.
play = ask_to_play(rounds, consecutive_correct)

# Start the game if the user says 'yes'.
while play.lower() not in ['n', 'no']:
    # Start the game.
    rounds += 1

    # Randomly roll six dice and store them in a list.
    diceList = []
    for _ in range(6):
        diceList.append(random.randint(1, 6))

    # Display the six generated dice rolls.
    dice.display_dice(diceList)

    # Petals calculation. 
    petals = calculate_petals(diceList)

    # Prompt for, read, and validate guess from the user.
    guess = validate_guess()

    # Compare the user's guess with the total petals calculated.
    if guess == petals:
        consecutive_correct += 1
        total_correct += 1
        if consecutive_correct % 4 == 0:
            print(
                'Congratulations! You have worked out the secret!\n'
                'Make sure you don\'t tell anyone!'
            )
            # Ask if the user wants to play again.
            play = ask_to_play(rounds, consecutive_correct)
        else:
            print('Well done! You guessed it!')
        # If the user has more than four correct guesses in a row.
        if consecutive_correct > 4:
            # Confirm four consecutive guesses.
            potentate = True
            # Ask if the user wants to play again.
            play = ask_to_play(rounds, consecutive_correct)
        
    else:
        consecutive_correct = 0
        print(f'No sorry, it\'s {petals} not {guess}.', end=' ')
        if guess % 2 != 0:
            print(f'The score is always even.')
        else:
            print() 
        print(
            '\nHint: The name of the game is important... '
            'Petals Around the Rose.'
        )
        # Ask if the user still wants to play again.
        play = ask_to_play(rounds, consecutive_correct)


# ------------------------------ Summary ------------------------------ #
if rounds:
    print(
        f'\n\nGame Summary',
        f'------------',
        f'You played {rounds} games:',
        f' * Correct guesses:     {total_correct}',
        f' * Incorrect guesses:   {rounds - total_correct}',
        sep='\n',
        end='\n\n',
    )
    if potentate:
        print('Congratulations, you are now a Potentate of the Rose.')
    else:
        print('Maybe you will work it out next time.')
    print('Thanks for playing!')
else:
    print('\nPlease play soon... :)')
