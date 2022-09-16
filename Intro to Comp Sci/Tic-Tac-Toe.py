"""
Pedro Torres
Tic Tac Toe Project

Goal: Use dictionaries to create a tic-tac-toe game that is played with 2 players

"""
# creating the dictionary to represent the board
# theBoard is a variable that represents a clear board that will be filled in as player makes moves

theBoard = {
    '1': " 1 ", '2': " 2 ", '3': " 3 ",
    '4': " 4 ", "5": " 5 ", '6': " 6 ",
    '7': " 7 ", '8': " 8 ", '9': " 9 ",
}

'''
Next, we will create a function that will print the board in such a way that it looks like an actual tic tac board.

We will call this function throughout the game whenever we want to print our updated board.
'''


def print_board(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('---+---+---')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---+---+---')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game_rules():
    print("Welcome!")
    print("")
    print("RULES:")
    print("Play fairly")
    print("Have fun")
    print("")


def check_winner():
    var = 0
    while var <= 6:
        if theBoard[str(var + 1)] == " X " and theBoard[str(var + 2)] == " X " and theBoard[str(var + 3)] == " X ":
            return "x"
        elif theBoard[str(var + 1)] == " O " and theBoard[str(var + 2)] == " O " and theBoard[str(var + 3)] == " O ":
            return "o"
        var = var + 3
    var = 0
    while var < 3:
        if theBoard[str(var + 1)] == " X " and theBoard[str(var + 4)] == " X " and theBoard[str(var + 7)] == " X ":
            return "x"
        elif theBoard[str(var + 1)] == " O " and theBoard[str(var + 4)] == " O " and theBoard[str(var + 7)] == " O ":
            return "o"
        var = var + 1
    if theBoard["1"] == " X " and theBoard["5"] == " X " and theBoard["9"] == " X ":
        return "x"
    elif theBoard["1"] == " O " and theBoard["5"] == " O " and theBoard["9"] == " O ":
        return "o"
    if theBoard["3"] == " X " and theBoard["5"] == " X " and theBoard["7"] == " X ":
        return "x"
    elif theBoard["3"] == " O " and theBoard["5"] == " O " and theBoard["7"] == " O ":
        return "o"
    return "none"


game_rules()
print("")


# =======================================================

# alternating X's and O's on the board
# 1st way:

def game():
    temp = 0
    counter = 0
    turn = " X "
    while counter < 9:
        print_board(theBoard)
        print("")
        while True:
            try:
                move = input("It is" + turn + "'s turn. What is your move?: ")
                move = int(move)
                if (move > 9) | (move < 1):
                    1/0
                break
            except:
                print("That not a valid entry, try again")

        # make sure the move is valid by error proofing
        move = str(move)
        if (theBoard[move] == " X ") or (theBoard[move] == " O "):
            print("Box already occupied, try again")
        else:
            theBoard[move] = turn
            if turn == " X ":
                turn = " O "
            else:
                turn = " X "
            counter = counter + 1
        isWinner = check_winner()
        if isWinner != "none":
            break


game()
winner = check_winner()
if winner == "x":
    print("X has won!")
elif winner == "o":
    print("O has won")
else:
    print("Game is a tie")
x = True
while x:
    playAgain = input("Would you like to play again: yes or no: ")
    if str(playAgain) == "yes" or str(playAgain) == "no":
        x = False
    else:
        print("choose 'yes' or 'no' ")
if playAgain == "no":
    print("have a good day")
else:
    theBoard = {
        '1': " 1 ", '2': " 2 ", '3': " 3 ",
        '4': " 4 ", "5": " 5 ", '6': " 6 ",
        '7': " 7 ", '8': " 8 ", '9': " 9 ",
    }
    game()
