from random import randint

#create board for gameplay

board = []

for i in range(0, 6):
    board.append(["O"] * 6)


def print_board(board):
    for row in board:
        print(" ".join(row))


print_board(board)


#create random ship placement


def rand_row(board):
    print(randint(0, len(board) - 1))


def rand_col(board):
    print(randint(0, len(board) - 1))


rand_row(board)


rand_col(board)