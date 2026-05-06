import random

level1 = [
    ["What is 1+1?", 2],
    ["What is 5-2?", 3],
    ["What is 6+7?", 13]
]

score = 0

while True:
    question, answer = random.choice(level1)
    user = input(f"{question} = ")

    try:
        user = int(user)
        if user == answer:
            print("That's correct!\n")
            score += 1
        else:
            print("Incorrect!\n")

    except ValueError:
        if user == "end":
            print(f"Score: {score}")
            break
        else:
            print("Please answer a number!\n")