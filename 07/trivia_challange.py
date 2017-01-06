# The Trivia Challenge game
# Trivia game that reads a plain text file


import sys, pickle

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
    line = line.replace("/", "\n")
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

    points = next_line(the_file)
    if points:
        points = points[0]

    explanation = next_line(the_file)
    return category, question, answers, correct, points, explanation

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
    user_name = input("Enter your username: ")

    # get first block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
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
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score: ", score, "\n\n")

        # get next block
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question for today!")
    print("Your final score is {}".format(score))

    if score >= 6:
        print("Congratz {}! Your score {} is recorded to the board of winners as a plain text and as a binary file.".format(user_name, score))
        data_to_save = user_name + ": " + str(score) + "\n"

        # writing data as plain text
        high_scores_file = open_file("high_scores.txt", "a")
        high_scores_file.write(data_to_save)
        high_scores_file.close()

        # writing data as binary file
        high_scores_dat = open("high_scores.dat", "wb+")
        pickled = pickle.dump(data_to_save, high_scores_dat)
        high_scores_dat.close()

        high_scores_dat = open("high_scores.dat", "rb")
        unpickled = pickle.load(high_scores_dat)
        print("Wow! I've just read this data from binary file:\n", unpickled)
        high_scores_dat.close()
    else:
        print("Sorry {}, your score {} won't be recorded, because it's too low. Try one more time to get 6 or more scores.".format(user_name, score))

main()
input("\n\nPress the enter key to exit.")


