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
    num1 = random.randint(low,high)
    num2 = random.randint(low,high)
    operator = random.choice(ops)

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

    # The question ig huhu
    question = f"What is {num1} {operator} {num2}?"

    return question, ans

#Integer checker to check if it's a number, and to return the exit code
def int_check(question, exit_code="xxx"):
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer that may be the correct answer(╯°□°）╯︵ ┻━┻"

    while True:
        try:
            response = input(question)

            # If users choice is the exit code, break the loop
            if response == "xxx":
                return exit_code

            response = int(response)
            return response

        except ValueError:
            print(error)

#Checks if it's a question
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

        #show error if response is no valid
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
     
    But please do know that you may need 
    to enter negative answers sometimes!

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
feedback = ""

quiz_history = []
all_user_answers = []

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
user_choice = string_checker("Please choose your difficulty level from (e)easy, (m)medium, (h)hard."
                             " WARNING! There are negative answers included in every lvl!: ", difficulty_list).strip().lower()
print("You choose: ", user_choice)
print()

#Ask user for number of rounds / infinite mode
print()
num_rounds = num_check("How many rounds would you like to play? Push <enter> for infinite mode: ",
                      exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

#Quiz variables again huhu
quiz_history = []
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

#Set correct answers and wrong answers to zero at the start of each round
correct_user_answers = []
incorrect_user_answers = []

while rounds_played < num_rounds:

    rounds_played += 1

    # Question Headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Question {rounds_played} (Infinite Mode)♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Question {rounds_played} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    question = generate_question()
    user_answer = int_check(question[0])

    #If users enter the exit code, break the loop >:)
    if user_answer == exit_code:
        break

    # If users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    #To check if you enter a number of not and shows you the answer
    if user_answer == question[1]:
        print(f"✅Correct! The answer is {question[1]}!✅")


    elif user_answer != question[1]:
        print(f"❌Incorrect! The answer is {question[1]}!❌")

    else:
        print("Please enter a number for goodness sake! ╰（‵□′）╯")

    #If users choice is the exit code, break the loop
    if user_answer == "xxx":
        break

    all_user_answers.append(user_answer)

#Game loop ends here
print()
print("The END of your Quiz! Yipe! (/≧▽≦)/")
print()

#Quiz history / Statistics here
# check users have played at least one round of the quiz
# before calculating statistics

#Add the round results to the quiz history
history_feedback = f"Questions {rounds_played}: {feedback}"
quiz_history.append(history_feedback)

#Add the answers that are correct to the score list
all_user_answers.append(user_answer)

# if users are in infinite increase number of rounds
if mode == "infinite":
    num_rounds += 1

if rounds_played > 0:

    # Game History / Statistics area

    # Calculate statistics
    all_user_answers.sort()
    correct_user_answers_score = correct_user_answers
    incorrect_user_answers_score = incorrect_user_answers
    average_score = sum(all_user_answers) / len(all_user_answers)

    # Ask if they want to see their quiz history
    # ask the user if they want instructions (check is they say yes / no)
    see_quiz_history = string_checker("Do you want to see your Quiz History? (*/ω＼*) ")

    # Display the instructions if the user wants to see them...
    if see_quiz_history == "yes":
        for item in quiz_history:
            print(item)

    # Output the statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Correct Answers╰(*°▽°*)╯:{correct_user_answers_score} | Worst╰（‵□′）╯:{incorrect_user_answers_score} | Average（*＾-＾*）:{average_score:.2f} ")
    print()
    print("I Hope you had fun! Have a lovely day superstar! (❁´◡`❁)")

