# Instructions

def yes_no(question):
    """Checks if user enters yes / no"""
    while True:

        response = input(question).lower()

        # Check if the user says yes / no / y / n
        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer the question, yes or no! Geez people! o(≧口≦)o")


def instructions():
    """prints instructions"""

    print("""
    *** Instructions ***

    To begin, Choose what Difficulty you want to play on! 
    Easy is Addition and Subtraction.
    Medium 2 is Multiplication Division.
    Hard is Basically both Level 1 and 2 combined!
            including all Basic operations!
    
    Choose now many rounds you'd like to play!
    <enter> for infinite mode!
    
    Then just do your best to answer the Questions 
    honestly, not my problems anymore ¯\_(ツ)_/¯
    (Totally no pun intended OwO )

     Good luck Superstar!

    """)


# Main routine
print()
print("🎊🎊WELCOME🎊🎊")
print("➕➖To The Basic Operations Game!✖️➗")
print()

# ask the user if they want instructions (check is they say yes / no)
want_instructions = yes_no("Do you want to see instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

