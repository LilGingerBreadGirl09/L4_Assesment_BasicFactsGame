import math
import random

#Checks of you enter a valid answer on questions asked :3
def string_checker(question, valid_ans=('yes', 'no')):

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


#Question generatorrrr AAAAAAA
def generate_question():
    num1 = random.randint(10,50)
    num2 = random.randint(low,high)
    operator = random.choice(ops)
    #The question ig huhu
    question = f"What is {num1} {operator} {num2}?"
    #The operations
    if operator=="+":
        ans = num1+num2
    elif operator=="-":
        ans = num1-num2
    elif operator=="x":
        ans = num1*num2
    else:
        ans = num1
        num1 = num1*num2


    return question, ans



#Checks if its a question
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





# Instructions
def instructions():
    """prints instructions"""

    print("""
    *** Instructions ***

    To begin, Choose what Difficulty you want to play on! 
    Easy is Addition and Subtraction.
    Medium is Multiplication Division.
    Hard is Basically both Level 1 and 2 combined!
            including all Basic operations!

    Choose now many rounds you'd like to play!
    <enter> for infinite mode!

    Then just do your best to answer the Questions 
    honestly, not my problems anymore (≧∇≦)
    (Totally no pun intended OwO )

     Good luck Superstar!

    """)



# Main routine

#Quiz variables?
difficulty_list = ["easy", "medium", "hard"]
mode = "regular"
rounds_played = 0


print()
print("🎊🎊WELCOME🎊🎊")
print("➕➖To The Basic Operations Game!✖️➗")
print()

# ask the user if they want instructions (check is they say yes / no)
want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

#Ask and get what lvl of difficulty the want
user_choice = string_checker("Please choose your difficulty level: ", difficulty_list).strip().lower()
print("You choose: ", user_choice)
print()

#Ask user for number of rounds / infinite mode
num_rounds = num_check("How many rounds would you like to play? Push <enter> for infinite mode: ",
                      exit_code="")



if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

#Quiz variables again huhu
ops = ["+", "-", "x", "÷"]
difficulty_list = ["easy", "medium", "hard"]

low = 1
high = None

if user_choice == difficulty_list[0]:
    high = 20
    ops = ["+", "-", ]
    exit_code = "xxx"

elif user_choice == difficulty_list[1]:
    high = 20
    ops = ["+", "-", ]
    exit_code = "xxx"

else:
    high = 30
    ops = ["+", "-", "x", "÷"]
    exit_code = "xxx"

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

    question = generate_question()
    user_answer = input(question[0])

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    #If users choice is the exit code, break the loop
    if user_answer == "xxx":
        break
