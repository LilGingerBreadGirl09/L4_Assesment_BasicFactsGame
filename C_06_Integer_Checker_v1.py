# #Checks if users enters an integer
# #that is more than 0

def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer that may be the correct answer(╯°□°）╯︵ ┻━┻"

    while True:
        try:
            response = int(input(question = generate_question()))

            if response != question[0]:
                print(error)

            else:
               return response

        except ValueError:
            print(error)
