from random import randint

# create board for gameplay

board = []


while True:
    board_size = int(input("What size board would you like to play? "))
    if board_size < 3 or board_size > 7:
        print("The board size needs to be between 3x3 and 7x7")
    else:
        break


for i in range(0, board_size):
    board.append(["O"] * board_size)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


# create random ship placement

ships_num = board_size


def rand_row(board):
    return randint(0, len(board) - 1)


def rand_col(board):
    return randint(0, len(board) - 1)


ship_row = rand_row(board)
ship_col = rand_col(board)

while board[ship_row][ship_col] == "O":
    guess_row = int(input("Guess the Row: "))
    guess_col = int(input("Guess the Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("You hit the battleship!")
        board[guess_row][guess_col] = "X"
    else:
        if guess_row > int(board_size) or guess_col > int(board_size):
            print("invalid guess")
        elif board[guess_row][guess_col] == "-":
            print("You have already guessed here")
        else: 
            print("You missed!")
            print(ship_row, ship_col)
            board[guess_row][guess_col] = "-"
            print_board(board)
else:
    print_board(board)
    print("You sunk the battleship! Well done!")