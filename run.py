from random import randint

# create board for gameplay

player_board = []
computer_board = []

while True:
    name_entry = input("What is your name? ")
    name = name_entry.capitalize()
    if name == "Computer":
        print("Thats my name! Try again")
    else:
        break


while True:
    board_size = int(input("What size board would you like to play? "))
    if board_size < 3 or board_size > 7:
        print("The board size needs to be between 3x3 and 7x7")
    else:
        break


for i in range(0, board_size):
    player_board.append(["O"] * board_size)

for i in range(0, board_size):
    computer_board.append(["O"] * board_size)


def print_player_board(player_board):
    print(f"{name}'s Board")
    for row in player_board:
        print(" ".join(row))

def print_computer_board(computer_board):
    print("Computer Board")
    for row in computer_board:
        print(" ".join(row))



print_player_board(player_board)
print("\n")
print_computer_board(computer_board)


# create random ship placement

ships_num = board_size


def rand_row_computer(computer_board):
    return randint(0, len(computer_board) - 1)


def rand_col_computer(computer_board):
    return randint(0, len(computer_board) - 1)

def computer_guess_row(player_board):
    return randint(0, len(player_board) - 1)

def computer_guess_col(player_board):
    return randint(0, len(player_board) - 1)


player_ship_row = rand_row_computer(computer_board)
player_ship_col = rand_col_computer(computer_board)

computer_ship_row = rand_row_computer(player_board)
computer_ship_col = rand_col_computer(player_board)
# Game logic to check if a guess is valid, miss or hit

while computer_board[computer_ship_row][computer_ship_col] == "O":
    guess_row = (int(input("Guess the Row: ")) - 1)
    guess_col = (int(input("Guess the Column: ")) - 1)

    if guess_row == computer_ship_row and guess_col == computer_ship_col:
        print("You hit the battleship!")
        computer_board[guess_row][guess_col] = "X"
    else:
        if guess_row > int(board_size - 1) or guess_col > int(board_size - 1):
            print("invalid guess")
        elif computer_board[guess_row][guess_col] == "-":
            print("You have already guessed here, try again")
        else: 
            print("You missed!")
            print(computer_ship_row, computer_ship_col)
            computer_board[guess_row][guess_col] = "-"
            print_computer_board(computer_board)
else:
    print_player_board(player_board)
    print_computer_board(computer_board)
    print(f"You sunk the battleship! Well done {name}!")