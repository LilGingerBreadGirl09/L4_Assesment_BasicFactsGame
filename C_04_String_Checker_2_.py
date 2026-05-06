#Check that the user entered like a valid answer ig?
#with an option on the list

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


lvl_difficulty_list = ["easy", "medium", "hard", "xxx"]

want_instructions = string_checker("Do you want to see the instructions? ")

print("You choose: ", want_instructions)

user_choice = string_checker("Please choose your difficulty level: ", lvl_difficulty_list)
print("You choose: ", user_choice)