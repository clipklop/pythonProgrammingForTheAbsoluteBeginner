# Guess My Number Game with GUI


import random
from tkinter import *


class Application(Frame):
    def __init__(self, master):
        """ Initialize Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.random_num = random.randint(1, 100)
        self.counter = 0
        self.create_widgets()
        self.reset_game


    def create_widgets(self):
        """ Create a GUI widgets for Guess My Number Game """
        # welcomes the user
        Label(self, text = "I'm thinking of a number between 1 and 100. Try to guess it in as few attempts as possible.") \
        .grid(row = 0, column = 0, columnspan = 4, sticky = W)

        Label(self, text = "").grid(row = 1, column = 0)

        # ask player for a guess number
        Label(self, text = "Take a guess:").grid(row = 2, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 2, column = 1, sticky = W)

        # record and display number of guesses
        Label(self, text = "Attempts:").grid(row = 2, column = 2, sticky = W)
        self.attempts_ent = Entry(self)
        self.attempts_ent.grid(row = 2, column = 3, sticky = W)

        # submit user guess
        Button(self, text = "Submit", command = self.take_guess) \
        .grid(row = 3, column = 1, sticky = W)

        # submit reset game
        Button(self, text = "Reset", command = self.reset_game) \
        .grid(row = 4, column = 1, sticky = W)

        # if type(self.guess_ent.get()) == int:
        #     self.counter += 1

        self.story_txt = Text(self, width = 80, height = 4, wrap = WORD)
        self.story_txt.grid(row = 5, column = 0, columnspan = 4)


    def take_guess(self):
        try:
            self.user_input = int(self.guess_ent.get())

            self.counter += 1
            self.attempts_ent.delete(0, END)
            self.attempts_ent.insert(0, self.counter)

            if self.user_input > self.random_num:
                self.story_txt.delete(0.0, END)
                self.story_txt.insert(0.0, "Your number is too high!")
            elif self.user_input < self.random_num:
                self.story_txt.delete(0.0, END)
                self.story_txt.insert(0.0, "Your number is too low!")
            else:
                self.story_txt.delete(0.0, END)
                self.story_txt.insert(0.0, "Congratz! You've won. The number was {} and it took {} attempts to guess it." \
                .format(self.random_num, self.counter))

        except ValueError:
            self.story_txt.delete(0.0, END)
            self.story_txt.insert(0.0, "Please enter a number.")


    def reset_game(self):
        self.story_txt.delete(0.0, END)
        self.random_num = random.randint(1, 100)
        self.guess_ent.delete(0, END)
        self.counter = 0
        self.attempts_ent.delete(0, END)
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, "The game was reseted, so the number also.")


def main():
    root = Tk()
    root.title("Guess My Number")
    app = Application(root)
    root.mainloop()

main()