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

print("Please input the name so the program will produce the name of his father.\n")

names_dad = {
    'Serg': 'Mikhail',
    'Misha': 'Serg',
    'Anya': 'Serg',
    'Senya': 'Misha',
    'Sasha': 'Andrey',
    'Anatoly': 'Valdimir',
    'Irina': 'Anatoly',
    'Polina': 'Anatoly',
    'Aleksy': 'Sergey',
    'Andrey': 'Sergey'
}

for son in names_dad.keys():
    print(son)

print("Write a name to found out who's father")