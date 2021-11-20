#!/usr/bin/env python3

#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         6/10/2021
# Description:  Build a mathematical challenging puzzle/game -
#               Petals Around The Rose.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.


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


def validateGuess():
    """Docstring for the function validateGuess().
    
    Validate guess from the user which should be a positive integer.

    Returns
    -------
    int
        The valid guess taken by the user.
    """
    guess = None
    
    while guess == None or guess < 0:
        try:
            guess = float(input('Please enter your guess for the roll: '))
            if guess < 0:
                print('Error: negative number')
        except ValueError as e:
            print('Error:', e)
        print()
    
    return int(guess)


def calculatePetals(diceList):
    """Docstring for the function calculatePetals().

    Calculate the number of petals around the rose.

    Parameters
    ----------
    diceList : list
        The list whose items are the values of the dice.

    Returns
    -------
    int
        The number of petals around the rose.
    """
    petals = 0 
    for face_value in diceList:
        if face_value == 3:
            petals += 2
        elif face_value == 5:
            petals += 4
        else:                   # face_value = 1, 2, 4, 6.
            petals += 0
    return petals


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
rounds = 0
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
    play = input('\nWould you like to play Petals Around the Rose [y|n]? ')
    while play.lower() not in ['y', 'yes', 'n', 'no']:
        print("Please enter either 'y' or 'n'.")
        play = input('\nWould you like to play Petals Around the Rose [y|n]? ')

    # Start the game if the user says 'yes'.
    while play.lower() not in ['n', 'no']:
        # Start the game.
        rounds += 1

        # Randomly roll six dice and store them in a list.
        diceList = []
        for _ in range(6):
            diceList.append(random.randint(1, 6))

        # Call the predefined function to display the generated dice rolls.
        dice.display_dice(diceList)

        # Petals calculation. 
        petals = calculatePetals(diceList)

        # Prompt for, read, and validate guess from the user.
        guess = validateGuess()

        # Compare the user's guess with the total petals calculated.
        if guess == petals:
            consecutive_correct += 1
            total_correct += 1
            if consecutive_correct == 4:
                print(
                    'Congratulations! You have worked out the secret!\n'
                    'Make sure you don\'t tell anyone!'
                )
                four_correct_in_row = True
            elif consecutive_correct > 0:
                print('Well done! You guessed it!')
        else:
            incorrect_guess = True
            if guess % 2 == 0:
                print(f'No sorry, it\'s {petals} not {guess}.')
            else:
                print(
                    f'No sorry, it\'s {petals} not {guess}. ' 
                    f'The score is always even.'
                )
            
            print(
                '\nHint: The name of the game is important... '
                'Petals Around the Rose.'
            )
            
        # Evaluate the guesses to display an appropriate message.
        if not incorrect_guess:
            if four_correct_in_row:
                """
                If the user has already guessed correctly four times in
                a row, and now another correct guess is made, mark this 
                event so that appropriate message can be displayed later.
                """
                more_than_4_correct_in_row = True
            
            # If the user has four or more correct guesses in a row.
            if consecutive_correct == 4 or more_than_4_correct_in_row:
                # Ask them if they want to replay the game.
                play = input('\nDo you want to keep playing [y|n]? ')
                while play.lower() not in ['y', 'yes', 'n', 'no']:
                    print("Please enter either 'y' or 'n'.")
                    play = input('\nDo you want to keep playing [y|n]? ')
                # Reset the variable before playing again.
                consecutive_correct = 0
        else:                   # If the user guessed incorrectly.    
            """
            This else branch prevents the event that the user responds
            'no' to the prompting message from the previous if branch.
            """
            if play not in ['n', 'no']:
                # Ask them if they want to stop playing.
                abort = False
                
                while not abort:
                    abort = input('\nDo you give up [y|n]? ')
                    while abort.lower() not in ['y', 'yes', 'n', 'no']:
                        print("Please enter either 'y' or 'n'.")
                        abort = input('\nDo you give up [y|n]? ')
                    """
                    Depending on the user choice, change the play variable 
                    so that the outer while loop can be iterated again.
                    """
                    if abort.lower() not in ['n', 'no']:
                        play = 'n'
                    else:
                        play = 'y'
                        # Reset the variable before playing again.
                        incorrect_guess = False

# Game summary.
if rounds:
    print(
    f"""\n
Game Summary
------------
You played {rounds} games:
 * Correct guesses:     {total_correct}
 * Incorrect guesses:   {rounds - total_correct}
    """
    )
    if more_than_4_correct_in_row:
        print('Congratulations, you are now a Potentate of the Rose.')
    else:
        print('Maybe you will work it out next time.')
    print('Thanks for playing!')
else:
    print('\nPlease play soon... :)')
