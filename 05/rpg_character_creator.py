# Write a Character Creator program for a role-playing game. The player
# should be given a pool of 30 points to spend on four attributes:
# Strength, Health, Wisdom, and Dexterity. The player should be able
# to spend points from the pool on any attribute and should also be able
# to take points from an attribute and put them back into the pool.

###
# Chapter 05
# Task 02: User get 30 points and can spend/take it back/reassign /
# it on attributes of character.
###

total_points = 30
attributes = {
    "health": 0,
    "strength": 0,
    "agility": 0,
    "intelligence": 0
}
menu_choice = None

while menu_choice != "0":
    print("""
You have 30 points to spend on characters attribute.
Please choose wisely.
--
Take your choice:
    Exit          --- 0
    Add points    --- 1
    Take points   --- 2
    Total points  --- 3
    """)
    menu_choice = input("\nYour choice please: ")
    if menu_choice == "0":
        print("Good bye, warrior.")
        break
    elif menu_choice == "1":
        if total_points != 0:
            print("""
                You have four attributes to upgrade:
                    health
                    strength
                    agility
                    intelligence
            """)
            attr_choice = input("What attribute you'd like to change? ").lower()
            if attr_choice in attributes:
                print("You have {} to spend on {}".format(total_points, attr_choice))
                points = int(input("How many points you would like to add? "))
                while points > total_points:
                    print("Sorry, you don't have that much. You have only {} points".format(total_points))
                    points = int(input("How many points you would like to add? "))
                attributes[attr_choice] += points
                total_points -= points
                print("Awesome! You have added {} points to {}".format(points, attr_choice))
                print("Here is your overal stats: \n{}".format(attributes))
                input("Press Enter to continue...")
            else:
                print("Sorry, no such attribute.")
        else:
            print("Sorry, no free points left")
            input("Press Enter to continue...")
    elif menu_choice == "2":
        print("health: {}".format(attributes["health"]))
        print("strength: {}".format(attributes["strength"]))
        print("agility: {}".format(attributes["agility"]))
        print("intelligence: {}".format(attributes["intelligence"]))
        attr_choice = input("From which attribute you would like to take points? ").lower()
        if attr_choice in attributes:
            print("You can take {} points from {}".format(attributes[attr_choice], attr_choice))
            points = int(input("How many points you would like to take back? "))
            if points <= attributes[attr_choice]:
                total_points += points
                attributes[attr_choice] -= points
                print("Ok, pal. You have took back {} points from {}".format(points, attr_choice))
                print("Here is your overal stats: \n{}".format(attributes))
                input("Press Enter to continue...")
            else:
                print("Sorry, the attribute {} doesn't have that much.".format(attr_choice))
                input("Press Enter to continue...")
        else:
            print("Sorry, no such attribute.")
    elif menu_choice == "3":
        print("The overall stats of total points:")
        for a, p in attributes.items():
            print("{}: {}".format(a, p))
        print("Points left: ", total_points)
        input("Press Enter to continue...")