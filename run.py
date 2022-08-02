#create board for gameplay

board = []

for i in range(0, 6):
    board.append(["O"] * 6)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)