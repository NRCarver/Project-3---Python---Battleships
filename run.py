from random import randint

# create board for gameplay

board = []

for i in range(0, 6):
    board.append(["O"] * 6)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


# create random ship placement


def rand_row(board):
    return randint(0, len(board) - 1)


def rand_col(board):
    return randint(0, len(board) - 1)


ship_row = rand_row(board)
ship_col = rand_col(board)

guess_row = int(input("Guess the Row: "))
guess_col = int(input("Guess the Column: "))

if guess_row == ship_row and guess_col == ship_col:
    print("You hit the battleship!")
else:
    if guess_row > int(6) or guess_col > int(6):
        print("invalid guess")
    else: 
        print("You missed!")
        print(ship_row, ship_col)
        board[guess_row][guess_col] = "X"
        print_board(board)