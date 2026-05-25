# #Checks if users enters an integer
# #that is more than 0

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
