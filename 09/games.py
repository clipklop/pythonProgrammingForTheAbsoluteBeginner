### A module for #blackjack game.
## Should demonstrate module creation ;)
#


class Player():
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name.title()
        self.score = score

    def __str__(self):
        output = self.name + ":\t" + str(self.score)
        return output

def ask_yes_no(question):
    """ Ask a question yes or no. """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """ Ask for a number within a range. """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == '__main__':
    print("Sorry, you ran this module directly, but should just 'import' it")
    input("\n\nPress any key to exit.")