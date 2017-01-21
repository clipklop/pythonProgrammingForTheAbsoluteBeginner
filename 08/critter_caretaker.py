### Critter Caretaker game
## A virtual pet to care for
#
# 1. Improve the Critter Caretaker program by allowing the user to specify how much
#   food he or she feeds the critter and how long he or she plays with the critter.
#   Have these values affect how quickly the critter’s hunger and boredom levels drop.
#
# 3. Create a “back door” in the Critter Caretaker program that shows the exact values
#   of the object’s attributes. Accomplish this by printing the object when a secret
#   selection, not listed in the menu, is entered as the user’s choice.
#   (Hint: add the special method __str__() to the Critter class.)
#
# 4. Create a Critter Farm program by instantiating several Critter objects and
#   keeping track of them through a list. Mimic the Critter Caretaker program,
#   but instead of requiring the user to care for a single critter, require them to
#   care for an entire farm. Each menu choice should allow the user to perform
#   some action for all of the critters (feed all of the critters, play with all of
#   the critters, or listen to all of the critters). To make the program interesting,
#   give each critter random starting hunger and boredom lev
#
##
###


class Critter(object):
    """Creating a class object for a virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        atrr_str = "Name: " + self.name + \
        "\nStarvation: " + str(self.hunger) + \
        "\nBoredum: " + str(self.boredom)
        return atrr_str

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m ="frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("\nI'm {} and I feel {} now.\n".format(self.name, self.mood))
        print("My current stats are: {} of hunger and {} of boredom\n".format(self.hunger, self.boredom))
        self.__pass_time()

    def eat(self, food = 4):
        print("Brrupp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Whee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("What do you want to name critter? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
            Critter Caretaker game

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
        """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Bye!")
        # listen to your critter
        elif choice == "1":
            crit.talk()
        # feed your critter
        elif choice == "2":
            how_much_food = int(input("How much kilos of food you want to give? "))
            if how_much_food > 1:
                crit.eat(how_much_food)
            else:
                crit.eat()
        # play with your critter
        elif choice == "3":
            how_much_play = int(input("How much time you want to spend for playing? "))
            if how_much_play > 1:
                crit.play(how_much_food)
            else:
                crit.play()
        # secret options that's not listed in menu to print object attributes
        elif choice == "4":
            print(crit)
        else:
            print("Sorry, but {} isn't a valid choice.".format(choice))

main()
("\n\nPress the enter key to exit.")



