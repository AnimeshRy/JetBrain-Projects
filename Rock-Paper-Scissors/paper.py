import random

rating = [line.split() for line in open("rating.txt", "r").readlines()]
rating = {name: int(score) for name, score in rating}

name = input("Enter your name: ")
print("Hello, {}".format(name))

if name in rating:
    score = rating[name]
else:
    score = 0

user = input()
options = {"paper": "rock", "rock": "scissors", "scissors": "paper"}

while user != "!exit":
    computer = random.choice(["rock", "paper", "scissors"])

    if options[computer] == user:
        print("Sorry, but computer chose {}".format(computer))
    elif user == computer:
        print("There is a draw ({})".format(computer))
        score += 50
    elif user in options and options[user] == computer:
        print("Well done. Computer chose {} and failed".format(computer))
        score += 100
    elif user == "!rating":
        print("Your rating: {}".format(score))
    else:
        print("Invalid input")

    user = input()

print("Bye!")
