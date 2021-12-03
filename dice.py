#
# Petals Around the Rose.
# Dice module - PSP Assignment 1, 2021.
#

# Function to display the face value of dice to the screen.
# This function takes a list of five numbers (the values of the five die to display) and
# displays the dice to the screen.
# Parameters:  A list containing 5 die face values, die1, die2, die3, die4, die5.
# Returns: Nothing is returned from the function.
def display_dice(dice):

    # Display die number to the screen.
    print("\n")
    print(format("", '<5s'), end='')
    for i in range(len(dice)):
        print(format("Die " + str(i+1), '<10s'), end='')
    print()

    # Display face value of die to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        print(format("[" + str(dice[i]) + "]", '<10s'), end='')
    print("\n")

    # Display the top row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1:
            print(format(" ", '<10s'), end='')
        elif dice[i] == 2 or dice[i] == 3:
            print(format("*", '<10s'), end='')
        elif dice[i] == 4 or dice[i] == 5 or dice[i] == 6:
            print(format("* *", '<10s'), end='')
    print()

    # Display the middle row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1 or dice[i] == 3 or dice[i] == 5:
            print(format(" *", '<10s'), end='')
        elif dice[i] == 6:
            print(format("* *", '<10s'), end='')
        else:
            print(format(" ", '<10s'), end='')
    print()

    # Display the bottom row of face value to the screen.
    print(format("", '<6s'), end='')
    for i in range(len(dice)):
        if dice[i] == 1:
            print(format(" ", '<10s'), end='')
        elif dice[i] == 2 or dice[i] == 3:
            print(format("  *", '<10s'), end='')
        elif dice[i] == 4 or dice[i] == 5 or dice[i] == 6:
            print(format("* *", '<10s'), end='')
    print("\n\n")
