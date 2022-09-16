"""
Rock Paper Scissor
Description: This program is a simple game of Rock Paper Scissors
Author: Pedro Torres
"""
import random


# This is a function that was created to convert any number from 1-3 to a string of 'rock', 'paper' or 'scissors'
def hand(num):
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"


# Prints the rules of the game
print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

while True:
    # Asks the User to pick and checks if their input is valid
    while True:
        print("Enter choice \n 1 for Rock \n 2 for paper \n 3 for scissor \n")
        selection = input("Input: ")
        if selection.isnumeric():
            selection = int(selection)
            if 3 >= selection >= 1:
                break
        print("Invalid response")

    # Uses the random integer function of the 'Random' library to pick a random number between 1 and 3
    cpu_selection = random.randint(1, 3)

    # Prints what you and the computer chose along with the final vs statement. Does so by using the hand function
    print("User chose " + hand(selection))
    print("Computer chose " + hand(cpu_selection))
    print(hand(selection) + " vs. " + hand(cpu_selection) + "\n")

    # chain of if/else statements that checks who won the game
    if cpu_selection == selection:
        result = 0
    elif cpu_selection == 1 and selection == 2 or cpu_selection == 2 and selection == 1:
        print("Paper wins ")
        result = 2
    elif cpu_selection == 1 and selection == 3 or cpu_selection == 3 and selection == 1:
        print("Rock wins ")
        result = 1
    elif cpu_selection == 2 and selection == 3 or cpu_selection == 3 and selection == 2:
        print("Scissors wins ")
        result = 3

    # Prints the winner/loser
    if result == selection:
        print("\n" + "Congrats, you won")
    elif cpu_selection == result:
        print("\n" + "Sorry, you lost")
    else:
        print("You have a tie!, you both chose " + hand(cpu_selection))

    # Asks user if they want to play again and checks if response is valid
    repeat = input("Play again? (Y/N) ").upper()
    while repeat not in ['Y', 'N']:
        repeat = input("Invalid response. Try Again: ").upper()
    if repeat == 'N':
        break
