# 1. Improve the function ask_number() so that the function
# can be called with a step value. Make the default value of step 1.

# 2. Modify the GuessMyNumber chapter project from Chapter 3 by reusing
# the function ask_number().

# 3. Modify the newversion of GuessMyNumber you created in the last
# challenge so that the program’s code is in a function called main().
# Don’t forget to call main() so that you can play the game.

# 4. Write a new computer_move() function for the Tic-Tac-Toe game
# to plug the hole in the computer’s strategy.
# See if you can create an opponent that is unbeatable!

import random

print('''
        Welcome to 'Guess My Number'!

I'm thinking of a number between 1 and 100
Try to guess it in as few attempts as possible.
''')

# Main function
def main():
    # pick a random number between 1 and 100
    the_number = random.randint(1, 100)

    # ask the player for a guess
    guess = int(input("Take a guess: "))

    # set the number of guesses to 1
    tries = 1

    # while the player's guess doesn't equal the number
    while guess != the_number:
        # if the guess is greater than the number
        if guess > the_number:
            # tell the player that the guess is too high
            print("Too high! Go lower...")
        # otherwise
        else:
            # tell the player to guess lower
            print("Too low! Go higher...")

        # get a new guess from the player
        # guess = int(input("Take a guess: "))
        guess = ask_number("Cmon, you can do it! Take a guess: ", 1, 100)

        # increase the number of guesses by 1
        tries += 1

        # congratulate the player on guessing the number
        # let the player know how many guesses it took
        if guess == the_number:
            print("You guessed it! The number was {}. It only took {} tries!".format(the_number, tries))
            print("Very good job!")
        elif tries == 6:
            print("You shall not pass!")
            break

#
def ask_number(question, low, high, step = 1):
    # ask for a number within the range
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

# Invoke our functions
main()
