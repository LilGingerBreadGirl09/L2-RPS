import random

# Check that users have entered a valid
# option based on a list

def string_checker(question,  valid_ans=('yes', 'no')):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word on the list
            if item == user_response:
                return item

            #check if the user response is the same as
            #the first letter or and item in the list
            elif user_response == item [0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()

# displays instructions
def instructions():
    """ prints instructions """

    print("""
*** Instructions ***

To begin, choose the number of rounds (or press <enter> for infinite mode).

Then play against the computer. You need to choose R (rock) P (paper) or S (scissors)

The rules are as follows:
o  Paper beats rock
o  Rock beats scissors
o  Scissors beats paper
""")


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

# Compares user / computer choice and returns
# Result ( win / lose / tie )
def rps_compare(user, comp):

   # If the user and the computer choice is the same, it's a tie
    if user == comp:
        round_result = "tie"

    # There are three ways to win
    elif user == "paper" and comp == "rock":
        round_result = "win"
    elif user == "scissors" and comp == "paper":
        round_result = "win"
    elif user == "rock" and comp == "scissors":
        round_result = "win"


    #If it's not a win / tie, then it's a loss
    else:
        round_result = "lose"

    return round_result



# Main routine starts here

# Intialise game variables
mode = "regular"

rounds_played = 0
rounds_tied = 0
rounds_lost = 0


rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []

print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()


# ask the user if they want instructions (check is they say yes / no)
# them if requested
want_instructions = string_checker("Do you want to see instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

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
    print()

    # randomly choose from the rps list (excluding the exit mode)
    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice", comp_choice)


    # Get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("you chose", user_choice)

    #If users choice is the exit code, break the loop
    if user_choice == "xxx":
        break

    result = rps_compare(user_choice, comp_choice)

    # Adjust game lost / game tied counters and add results to game history
    if result == "tie":
        rounds_tied += 1
        feedback = "👔👔 It's a Tie! 👔👔"
    elif result =="lose":
        rounds_lost += 1
        feedback = "🥲🥲You Lose...🥲🥲"
    else:
        feedback = "👍🥳You won!!!🥳👍"

    # Set up round feedback and output it user.
    # Add it to the game history list (include the round number)
    round_feedback = f"{user_choice} vs {comp_choice}, {feedback}"
    history_item = f"Round: {rounds_played} - {round_feedback}"

    print(round_feedback)
    game_history.append(history_item)

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1




#Game loop ends here

#Game history / Statistics here


# Calculate Statistics
round_won = rounds_played - rounds_tied - rounds_lost
percent_won = round_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100
percent_tied = 100 - percent_won - percent_lost

#Output Game Statistics
print("🔢🔢🔢 Game Statistics 🔢🔢🔢")
print(f"👍 Won: {percent_won:.2f} \t "
      f"🥲 Lost: {percent_lost:.2f} \t"
      f"👔 Tied {percent_tied:.2f}")

# ask user if they want to see their game history and output it if requested.
see_history = string_checker("\nDo you want to see your game history? ")
if see_history == "yes":
    for item in game_history:
        print(item)

    print()
    print("Thank you for Playing!")

else:
    print("🐔🐤🐣Oppsie, my gal, You chickened out! HAHA!🐣🐤🐔")





