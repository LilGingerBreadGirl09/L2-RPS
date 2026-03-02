#functions go here


def yes_no(question):
    """ Checks if user enters yes / no """
    while True:

        response = input(question).lower()

        #check the user says yes / no / y / n
        if response == "yes" or response == "y":
           return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes or No >:[")

def instructions():
    """ prints instructions """

    print("""
*** Instructions ***

Roll the Dice and try again!
""")


#Main routine

# ask the user if they want instructions (check is they say yes / no)
want_instructions = yes_no ("Do you want to see instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program Continues")