#Checks if you entered more than zero
#allows for us to have an exit code :3
def num_check(question, num_type=int, low=0, exit_code="xxx"):
    error = f"Please enter and integer that's more than {low}! o(≧口≦)o"

    while True:
        #Ask the user the question and return a response if
        #exit code is entered
        response = input(question)
        if response == exit_code:
            return response

        #Check response is more than 0 (min)
        try:
            response = num_type(response)

            if response > low:
                return response
            else:
                print(error)

        #show eroe if response is no valid
        except ValueError:
            print(error)



# Intialise game variables
mode = "regular"
rounds_played = 0

#Ask user for number of rounds / infinite mode
num_rounds = num_check("How many rounds would you like to play? Push <enter> for infinite mode: ",exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5
# If users are in infinite mode, increase number of rounds!

if mode == "infinite":
    num_rounds += 1

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

