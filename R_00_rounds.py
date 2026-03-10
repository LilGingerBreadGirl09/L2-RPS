# Check that users have entered a valid
# option based on a list
def int_check(question):
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 1. >:["

    while True:

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)

            else:
               return response

        except ValueError:
            print(error)




# Main routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# Instructions

#Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like to play? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

#Game loop starts here
while rounds_played < num_rounds:

    rounds_played += 1

    # Round Headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played} (Infinite Mode)♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    user_choice = input("Choose: ")
    print(f"you chose {user_choice}")

    if user_choice == "xxx":
        break

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1


#Game loop ends here

#Game history / Statistics here