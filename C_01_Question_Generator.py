import random
import math

#Question generatorrrr AAAAAAA
def generate_question():
    num1 = random.randint(1,50)
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


ops= ["+","-","x","÷"]
difficulty_list = ["easy", "medium", "hard"]

low = 1
high = None
user_difficulty = str(input("What is your difficulty?")).strip().lower()

if user_difficulty == difficulty_list[0]:
    high = 20
    ops = ["+", "-",]

elif user_difficulty == difficulty_list[1]:
    high = 20
    ops = ["+", "-",]

else:
    high = 30
    ops = ["+", "-", "x", "÷"]

question = generate_question()
user_ans = input(question[0])

