"""
Guessing Game
Description: This program is a simple guessing game with three different difficulties
Author: Pedro Torres
"""
from random import *

# Guessing Game 2.0

# Makes sure that the user enters a valid difficulty
options = ["Easy", "Medium", "Hard"]
while True:
    game_difficulty = input("Select a difficulty [Easy][Medium][Hard]: ")
    print("")
    game_difficulty = game_difficulty.capitalize()

    if game_difficulty in options:
        break
    else:
        # These are the exceptions
        if game_difficulty.isdigit():
            print("Enter a word not a number.")
            print("")
        else:
            print("Sorry, but that is not a valid difficulty.")
            print("")

guesses = 0
random_number = 0
guessing_range = 0
if game_difficulty == "Easy":
    guessing_range = 100
    guesses = 15
    random_number = randint(1, guessing_range)
elif game_difficulty == "Medium":
    guessing_range = 300
    guesses = 10
    random_number = randint(1, guessing_range)
elif game_difficulty == "Hard":
    guessing_range = 500
    guesses = 5
    random_number = randint(1, guessing_range)

print("You have chosen " + game_difficulty + " mode.")
print(str(guesses) + " guesses" + ".")
print("The random number lies between 1 and " + str(guessing_range) + ".")
print("\n")

# Starts the game
i = guesses
while i > 0:
    while True:
        try:
            print("")
            guess = int(input("Take your shot: "))
            break
        except ValueError:
            print("That input is invalid! Try something else.")
    if guess == random_number:
        print("You won!")
        break
    elif guess > guessing_range or guess < 0:
        print("You guess is out of range!")

    elif guess < random_number:
        i = i - 1
        print("You have guessed too low.")

    elif guess > random_number:
        i = i - 1
        print("You have guessed too high.")

    print(str(i) + " guesses left.")

if i > 0:
    print("You won!")
else:
    print("Wow, I guess you lost. Try again.")