# Checks users if they enter an answer

#
# #The list of lvls
# lvl_difficulty_list = (easy, medium, hard)

# Checks users if they enter an answer on what difficulty they want
def string_checker(question, valid_ans=(easy, medium, hard)):
    error = (f"Sorry - your response is not valid! "
             f"Please choose an item from this list: \n{valid_responses}. ")

    while True:
        # Making sure if its lower case
        response = input(question).lower()

        for item in valid_ans:
            # Check if the user response is a word on the list
            if item == user_response:
                return item

            # Check if the user response is the same as the
            # First letter or and item in the list
            elif user_response == item[0] or response == item:
                return item

        return "Invalid response, Please enter a VALID response!`(*>﹏<*)′"


# #Ask user what lvl they want to play
# lvl_list = string_checker(print("What level do you want to play today? (*^▽^*) "))
#
# if lvl_list == "easy":
#     mode = "easy"
#     print(easy)
# if lvl_list == "medium":
#     mode = "medium"
#     print(medium)
# if lvl_list == "hard":
#     mode = "hard"
#     print(hard)
#
#
#Auto mated testing
to_test = [
    ("Easy", "easy"),
    ("Medium", "medium"),
    ("Hard", "hard"),
    ("E", "easy"),
    ("x", "xxx"),
    ("random", "invalid"),
]

# run tests!
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case,("easy", "medium", "hard"))


    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f" ✅✅✅Passed! Case: {case}, expected: {expected}, received: {actual} ✅✅✅")
    else:
        print(f"❌❌❌ Failed! Case: {case}, expected: {expected}, received: {actual} ❌❌❌")







