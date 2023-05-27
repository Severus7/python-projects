import random

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
computerInput = random.randint(0,2)

choices = ["rock", "paper", "scissors"]

print(f"You have chosen: {choices[userInput]}")
print(f"Computer have chosen: {choices[computerInput]}")

if choices[userInput] == "rock":
    if choices[computerInput] == "paper":
        print("You lose!")
    elif choices[computerInput] == "scissors":
        print("You won!")
    else:
        print("Draw!")
elif choices[userInput] == "paper":
    if choices[computerInput] == "rock":
        print("You won!")
    elif choices[computerInput] == "scissors":
        print("You lose!")
    else:
        print("Draw!")
elif choices[userInput] == "scissors":
    if choices[computerInput] == "paper":
        print("You won!")
    elif choices[computerInput] == "rock":
        print("You lose!")
    else:
        print("Draw!")
else:
    print("Draw!")