"""My Quizzical Integration Project. This program is a simple quiz game about
Python and other random topics) Citations for helpers and sources: Malakai
Dragstrem, Erick Rodriguez,
Pogils 1-17, W3 Schools"""
__author__ = "Javier Duszynski"


def main():
    """The purpose of this main function is a quiz program that asks the
    user various questions and then takes in user input to return answers.
    The program runs in a while loop to continue until user enters the input no
    when prompted.
    """
    print("Welcome to my integration project!")
    user_name = input("Enter name: ")
    continue_program = True
    # The "While" loop here runs the program until the user kills the
    # program or makes it back to the "play" prompt and inputs "no" to quit.
    while continue_program:
        play = input(
            "\nI want to play a game.\nPlay this quiz? If you don't want to "
            "play, enter no otherwise press enter ")
        if play.lower() == "no":
            # here the relational operator "==" in "== "no"" verifies that if
            # the user enters "no" the program ends
            continue_program = False
        else:
            print("\nThen good luck", user_name)
            print("After entering your answer continue to press enter to "
                  "get to the next question or to move through the quiz. ")

            input("\nPress enter when ready ")
            # Here I assign player score to the value 0
            player_score = 0

            print("\nQuestion 1:\n")
            print("loop-the" * 5)
            # In this line ^ I used the "*" string repetition operator to
            # spam the string 5 times
            print("\nWhat string operator is used to repeat the string? ")
            answer = input("Enter your answer here: ")
            if answer == "*":
                print("Nice!")
                player_score += 1
            # The shortcut operator "+=" ads 1 to the player score total
            else:
                print("Nope, that's incorrect! The answer was *")

            input(" ")
            print("\nQuestion 2:\n")
            print("Hi", user_name, sep='')
            # I use sep='' here to change the comma's functionality
            answer = input(
                "\nThere is only a comma between Hi and your name in the "
                "print "
                "statement. \nWhat Python parameter achieves this? ")
            if answer == "sep=''":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was sep=''")

            input(" ")

            print("\nQuestion 3:\n")
            print("I like to swim", end=',')
            # using end=',' here causes I like to swim,do you like to? to be
            # printed
            print("do you like to?")
            print(
                "\nThe text ~I like to swim~ and ~do you like to?~ were "
                "separate \nprint "
                "statements on separate lines.")
            answer = input("\nWhat Python parameter causes them to be put "
                           "together with a "
                           "comma? ")
            if answer == "end=''":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was end=''")

            input(" ")

            print("\nQuestion 4:\n")
            print("Ha" + "Ha")
            # Using + here to create the output "HaHa" for the question
            print("\nThe two Ha in HaHa were once separate.")
            answer = input("\nWhat string operator concatenated the two Ha? ")
            if answer == "+":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was +")

            input(" ")

            print("\nQuestion 5:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input("Enter another whole number "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 * question_input_2)
            # Here I used the * numeric operator to make the program
            # multiply the user's two numeric inputs
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "*":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was *")

            input(" ")

            print("\nQuestion 6:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input("Enter another whole number "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 ** question_input_2)
            # Here I used the ** numeric operator to make the program
            # exponentiate the user's two numeric inputs
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "**":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was **")

            input(" ")

            print("\nQuestion 7:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input("Enter another whole number "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 - question_input_2)
            # Here I used the - numeric operator to make the program
            # subtract the user's second numeric input from the first
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "-":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was -")

            input(" ")

            print("\nQuestion 8:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input("Enter another whole number "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 / question_input_2)
            # Here I used the / numeric operator to make the program divide
            # the user's first numeric input by the second
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "/":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was /")

            input(" ")

            print("\nQuestion 9:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input(
                "Enter a whole number that does not go into the first number "
                "an equal\n "
                "amount of times "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 // question_input_2)
            # Here I used the // numeric operator to make the program divide
            # and round the user's first numeric input by the second
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "//":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was //")

            input(" ")

            print("\nQuestion 10:\n")
            question_input_1 = int(input("Enter a whole number "))
            question_input_2 = int(input(
                "Enter a whole number that does not go into the first number "
                "an equal\n "
                "amount of times "))
            print("\nPython computes the two numbers and outputs...")
            print(question_input_1 % question_input_2)
            # Here I used the % numeric operator to make the program divide
            # the user's first numeric input by the second and give the
            # remainder amount
            answer = input("\nWhat numeric operator in python caused this "
                           "answer? ")
            if answer == "%":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was %")

            input(" ")

            print("\nQuestion 11: Bonus Question!:\n")
            answer = input(
                "\nWhat word is always spelled incorrectly in every single "
                "dictionary? ")
            if answer.lower() == "incorrectly":
                print("Nice!")
                player_score += 1
            else:
                print("Nope, that's incorrect! The answer was incorrectly")

            input(" ")

            print("You got " + str(
                player_score) + " questions right!! good job!")
            print("You received a " + str((player_score / 11) * 100) + "%!")
            # Here I divide player score by 11 and multiply it by 100 to get
            # a percentage.

            print("\nContinue on for some bonus activities")

            input(" ")

            print("\nBonus Stuff!:\n")
            color = input("What is your favorite color? ")
            if color.lower() == "black":
                print("Nice. That's my second favorite color next to red. "
                      "You're pretty cool.")
                # Used elif for the first time here for another unique output
            elif color.lower() == "red":
                print("You are literally awesome. Red is indeed the best :).")
            else:
                print("Ehh not bad. Not my cup of tea though")

            input(" ")

            print("\nCan you guess the function used to create this list?\n")
            # The "range" function is used here with the iterative structures
            # "for" and "in" to display the numbers 1-9, exclusive of 10
            x = range(10)
            for n in x:
                print(n)
            bonus_input = input("Enter answer: ")
            # Here the relational operator "!=" specifies what to output if
            # the user does not input "range"
            if bonus_input.lower() != "range":
                print("Nope")
            else:
                print("Epic")

            input(" ")

            print("\nProvide the number of the month of your birthday.\n")
            month = int(input("Enter a month number from 1-12: "))
            # The boolean operator "or" is used here to define the
            # boundaries of input I am looking for
            if month > 12 or month < 1:
                print("Lol fine then. No bonus activity for you. :|")
            elif month == 1:
                print("Your birthstone is Garnet")
            elif month == 2:
                print("Your birthstone is Amethyst (Just like mine!)")
            elif month == 3:
                print("Your birthstone is Aquamarine")
            elif month == 4:
                print("Your birthstone is Diamond")
            elif month == 5:
                print("Your birthstone is Emerald")
            elif month == 6:
                print("Your birthstone is Alexandrite")
            elif month == 7:
                print("Your birthstone is Ruby")
            elif month == 8:
                print("Your birthstone is Peridot")
            elif month == 9:
                print("Your birthstone is Sapphire")
            elif month == 10:
                print("Your birthstone is Tourmaline")
            elif month == 11:
                print("Your birthstone is Topaz")
            else:
                print("Your birthstone is Blue Topaz")

            print("\nBirthstone months are according to gemsociety.org")

            input("")

            print(not False)
            # The boolean operator "not" outputs the opposite of False here,
            # which is true
            bonus_not = input("The word False was attached to an operator to "
                              "output the result above. Which operator? ")

            if bonus_not == "not":
                print("Nice.")
            else:
                print("Nah")

            print("\nLastly, binary.\n")

            binary_2 = int(input("Enter a base 10 number that is between the "
                                 "binary numbers 111100 and 1000110 "))
            # The "and" operator here specifies that the input has to fall
            # into two categories at the same time to be correct
            if 60 < binary_2 < 70:
                print("Excellent!")
            else:
                print("Not quite. Touch up on your binary!")

            input("\nThat's all for now folks!, thanks for playing!\nPress "
                  "Enter to play again ")


# This function with parameter passing displays a cheeky "Hello There" at
# the start of the program
def obiwan(hello):
    """This program greets the user upon running the program with the
    message 'Hello There'

    :param hello:
    :return: Hello There
    """
    #       ^ parameter
    return '{} There'.format(hello)


print(obiwan('Hello'))
#              ^ argument
# CALL TO MAIN
if __name__ == "__main__":
    main()
