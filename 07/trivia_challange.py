# The Trivia Challenge game 
# Trivia game that reads a plain text file


import sys

# function should return corresponding file object
# with try/except block to check if file exist
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file {}. Ending the program with an error:\n{}".format(file_name, e))
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

# recive a file a returns the formatted next line of text from it 
def next_line(the_file):
    line = the_file.readline()
    line = the_file.replace("/", "\n")
    return line

# reads the block of text lines and returns four strings(category, question, correct answer, explanation)
# and a list of for strings(possible answers)
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    
    answers = []
    for _ in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)
    return category, question, answers, correct, explanation

# welcomes the player with the episode title
def welcome(title):
    print("""
                Welcome to Trivia Challenge!
                {}
        """.format(title))

# Main func which looping whole game
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        #ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += 1
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score: ", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question for today!")
    print("Your final score is {}".format(score))

main()
input("\n\nPress the enter key to exit.")


