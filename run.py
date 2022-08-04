from random import randint


# Function for computer guesses
def print_player_board(player_name, player_board):
    print(f"{player_name}'s Board")
    for row in player_board:
        print(" ".join(row))


def print_computer_board(computer_board):
    print("Computer Board")
    for row in computer_board:
        print(" ".join(row))


def computer_guess(player_name, player_board, player_ship_row, player_ship_col):
    computer_guess_row = fcomputer_guess_row(player_board)
    computer_guess_col = fcomputer_guess_col(player_board)
    while player_board[player_ship_row][player_ship_col] == "O":
        if (computer_guess_row == player_ship_row) and (
                computer_guess_col == player_ship_col):
            print("Computer guessed ({}, {})".format(
                computer_guess_row, computer_guess_col))
            print("Computer hit your battleship!")
            player_board[computer_guess_row][computer_guess_col] = "X"
            print_player_board(player_name, player_board)
            break
        elif player_board[computer_guess_row][computer_guess_col] == "-":
            # computer_guess()
            pass
        else:
            print(f"""Computer guessed (
                {computer_guess_row},{computer_guess_col})""")
            print("Computer missed your ship!")
            print("You ship is placed at coordinates ({}, {})".format(
                player_ship_row, player_ship_col))
            print(player_ship_row, player_ship_col)
            player_board[computer_guess_row][computer_guess_col] = "-"
            print_player_board(player_name, player_board)
            break


def rand_row_computer(computer_board):
    return randint(0, len(computer_board) - 1)


def rand_col_computer(computer_board):
    return randint(0, len(computer_board) - 1)


def fcomputer_guess_row(player_board):
    return randint(0, len(player_board) - 1)


def fcomputer_guess_col(player_board):
    return randint(0, len(player_board) - 1)


def main():
    """
    """
    while True:
        # create board for gameplay

        player_board = []
        computer_board = []

        # Enter your name

        while True:
            name_entry = input("What is your name?\n")
            name = name_entry.capitalize()
            if name == "Computer":
                print("Thats my name! Try again")
            else:
                break

        # Choose the size of board you want to play on.
        while True:
            try:
                board_size = int(
                    input("What board size would you like to play?\n"))
                if board_size < 3 or board_size > 7:
                    print("The board size needs to be between 3x3 and 7x7")
                else:
                    break
            except ValueError:
                print("Please enter an integer between 3 and 7")

        # Create your board and the computer board

        for i in range(0, board_size):
            player_board.append(["O"] * board_size)

        for i in range(0, board_size):
            computer_board.append(["O"] * board_size)

        # Functions to print your board and the computer board

        # create random ship placement

        ships_num = (board_size - 2)
        print(ships_num)

        # Print player and computer boards

        print_player_board(name, player_board)
        print("\n")
        print_computer_board(computer_board)

        # Create coordinates for player ships and computer ships
        player_ship_row = rand_row_computer(computer_board)
        player_ship_col = rand_col_computer(computer_board)

        computer_ship_row = rand_row_computer(player_board)
        computer_ship_col = rand_col_computer(player_board)

        print("You ship is placed at coordinates ({}, {})".format(
            player_ship_row,
            player_ship_col
            ))

        # Game logic to check if a guess is valid, miss or hit and end game

        while computer_board[computer_ship_row][computer_ship_col] == "O":
            if player_board[player_ship_row][player_ship_col] == "X":
                print("You lost the game!")
                break
            else:
                try:
                    guess_row = int(input("Guess the Row:\n"))
                    guess_col = int(input("Guess the Column:\n"))
                    if (guess_row == computer_ship_row) and (
                            guess_col == computer_ship_col):
                        print("You hit the battleship!")
                        computer_board[guess_row][guess_col] = "X"
                    else:
                        if (guess_row > int(board_size - 1)) or (
                                guess_col > int(board_size - 1)):
                            print("invalid guess")
                        elif computer_board[guess_row][guess_col] == "-":
                            print("You have already guessed here, try again")
                        else:
                            print(f"You guessed ({guess_row},{guess_col})")
                            print("You missed!")
                            print(computer_ship_row, computer_ship_col)
                            computer_board[guess_row][guess_col] = "-"
                            computer_guess(name, player_board, player_ship_row,
                                           player_ship_col)
                            print_computer_board(computer_board)
                except ValueError:
                    print("Please enter a valid coordinate")
        else:
            print_player_board(name, player_board)
            print_computer_board(computer_board)
            print(f"You sunk the battleship! Well done {name}!")

        # Restart the game or not
        print("Game Over, would you like to play again or close the game?")
        restart = input("Enter 'Y' to restart or any other key to quit\n")

        if restart != "Y":
            break


main()
