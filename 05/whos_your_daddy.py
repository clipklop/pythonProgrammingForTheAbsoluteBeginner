# Write a Who’s Your Daddy? program that lets the user enter
# the name of a male and produces the name of his father. (You
# can use celebrities, fictional characters, or even historical
# figures for fun.) Allow the user to add, replace, and delete sonfather
# pairs.
# Improve the Who’s Your Daddy program by adding a choice that
# lets the user enter a name and get back a grandfather. Your
# program should still only use one dictionary of son-father
# pairs. Make sure to include several generations

###
# Chapter 05
# Task 03: When user inputs the name, the programm prints out his
# fathers name.
# Task 04: Add additional functionality to the program, so it's also
# should prints out the grandfathers name. You should use same dict.
###

print("Please input the name so the program will produce the name of his father.")
print("--")
names_dad = {
    'Serg': ('Mikhail', 'Sirafim'),
    'Misha': ('Serg', 'Mikhail'),
    'Anya': ('Serg', 'Mikhail'),
    'Senya': ('Misha', 'Serg'),
    'Sasha': ('Andrey', 'Unknown'),
    'Anatoly': ('Vladimir', 'Unknown'),
    'Irina': ('Anatoly', 'Valdimir'),
    'Polina': ('Anatoly', 'Vladimir'),
    'Aleksy': ('Sergey', 'Vladimir'),
    'Andrey': ('Sergey', 'Vladimir'),
    'Natasha': ('Igor', 'Unknown')
}

for son in names_dad.keys():
    print(son)

print("Write a name to found out who's father")
get_name = input("Give me a name, please: ").title()
if get_name in names_dad.keys():
    print("{}'s father is {}.".format(get_name, names_dad[get_name][0]))
    grand = input("Do you wanna know who was his grandfather? Y/n ")
    if grand == 'y':
        print("{}'s grandfather is {}.".format(get_name, names_dad[get_name][1]))
    elif grand == 'n':
        print("Bye, pal")
else:
    print("Sorry, I can't find {} in my database.".format(get_name))

# a little bit slacking with doing a task, such as performing a loop
# but I've already did it in rpg_character script.
