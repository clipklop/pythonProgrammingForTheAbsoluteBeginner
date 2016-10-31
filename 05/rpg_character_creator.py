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
        \n--
        Take your choice:
            Exit            - 0
            Add points      - 1
            Take points     - 2
            Total points    - 3
    """)
    menu_choice = input("\nYour choice please: ")
    if menu_choice == "0":
        print("Good bye, warrior.")
        break
    elif menu_choice == "1":
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
            attributes[attr_choice] = points
            total_points -= points
            print("Awesome! You have added {} points to {}".format(points, attr_choice))
            print("Here is your overal stats: \n{}".format(attributes))
            input("Press Enter to continue...")
        else:
            print("Sorry, no such attribute.")

### Not mine. Needs to be rewrited
#     elif user_input == 2:
#         attrib = input('Which attribute would you like to take points from? ')
#         attrib = attrib.lower()
#         if attrib in attributes:
#             points = int(input('\nHow many points would you like to take? '))
#             if points > attributes[attrib]:
#                 total += attributes[attrib]
#                 attributes[attrib] = 0
#                 print('\n You had less than', points,'in',attrib.title(),'so all the'\
#                       ' points in', attrib.title(),'have been taken and added back to your'\
#                       ' total to spend')
#             else:
#                 total += points
#                 attributes[attrib] -= points
#         else:
#             print('\nSorry that isn\'t a valid selection')
#     elif user_input == 3:
#         print('Attribute Totals:\n')
#         print('ATTRIBUTE\tPOINTS')
#         for attribute, points in attributes.items():
#             print(attribute, '\t', points)
#         print('Total\t', total)
#     else:
#         print('\nSorry that isn\'t a valid option')


# # let's user exit program
# input('Press enter to exit')


# Write a Character Creator program for a role-playing game. The player
# should be given a pool of 30 points to spend on four attributes:
# Strength, Health, Wisdom, and Dexterity. The player should be able
# to spend points from the pool on any attribute and should also be able
# to take points from an attribute and put them back into the pool.
