from random import randint

COMPUTER_NAME = "Computer"


def print_board(player_name, board):
    """
    Print the Player or Computer board
    """
    print(f"{player_name}'s Guessing Board")
    for row in board:
        print(" ".join(row))


def initialize_board(board, board_size):
    """
    Create the Player or Computer board
    """
    for i in range(0, board_size):
        board.append(["O"] * board_size)


def check_guess(player_name, target_row, target_col, c_row,
                c_col, h_row, h_col):
    """
    Return -1 if Human hit; 1 if Computer hit; 0 otherwise
    """
    if player_name == COMPUTER_NAME:
        if target_row == h_row and target_col == h_col:
            return 1
    else:
        if target_row == c_row and target_col == c_col:
            return -1
    return 0


def rand_value(board_size):
    """
    Generate random value
    """
    return randint(0, board_size - 1)


def input_value(msg):
    while True:
        try:
            value = int(input(msg))
            return value
        except ValueError:
            print("Please enter a valid coordinate")


def main():
    """
    Game function
    """
    print("-" * 50)
    print(" Welcome to  BATTLESHIPS!!\n")
    print(" To start, you will need to enter your name and board width.")
    print(" The board size can range from 3x3 to 7x7\n")
    print(" Note: The top left corner coordinate is row: 0, col: 0\n")
    print(" Good luck and enjoy the game!")
    print("-" * 50)
    while True:
        # create board for gameplay

        player_board = []
        computer_board = []

        # Enter your name

        while True:
            name_entry = input("What is your name?\n")
            name = name_entry.capitalize()
            if name == COMPUTER_NAME:
                print("\nThats my name! Try again")
            if name == "":
                continue
            else:
                break

        # Choose the size of board you want to play on.
        while True:
            try:
                board_size = int(
                    input("\nWhat board size would you like to play?\n"))
                if board_size < 3 or board_size > 7:
                    print("The board size needs to be between 3 and 7")
                else:
                    break
            except ValueError:
                print("The board size needs to be between 3 and 7")

        # Create your board and the computer board
        initialize_board(player_board, board_size)
        initialize_board(computer_board, board_size)

        # Print player and computer boards

        print_board(name, player_board)
        print("\n")
        print_board(COMPUTER_NAME, computer_board)

        # Create coordinates for player ships and computer ships
        player_ship_row = rand_value(board_size)
        player_ship_col = rand_value(board_size)

        computer_ship_row = rand_value(board_size)
        computer_ship_col = rand_value(board_size)

        print("You ship is placed at coordinates ({}, {})\n".format(
            player_ship_row,
            player_ship_col
        ))

        print("Computer ship is placed at coordinates ({}, {})\n".format(
            computer_ship_row,
            computer_ship_col
        ))

        # Game logic to check if a guess is valid, miss or hit and end game
        human_playing = True
        game_over = False
        while not game_over:
            if human_playing:
                guess_row = input_value("Guess the Row:\n")
                while not int(guess_row) in range(0, board_size):
                    print("That is not a valid row coordinate")
                    guess_row = input_value("Guess the Row:\n")
                guess_col = input_value("Guess the Column:\n")
                while not int(guess_col) in range(0, board_size):
                    print("That is not a valid column coordinate")
                    guess_col = input_value("Guess the Column:\n")
                if player_board[guess_row][guess_col] == "-":
                    print("You have tried there already!")
                    continue
            else:
                guess_row = rand_value(board_size)
                guess_col = rand_value(board_size)
                while computer_board[guess_row][guess_col] == "-":
                    guess_row = rand_value(board_size)
                    guess_col = rand_value(board_size)

            result = check_guess(
                name if human_playing else COMPUTER_NAME,
                guess_row,
                guess_col,
                computer_ship_row,
                computer_ship_col,
                player_ship_row,
                player_ship_col
            )

            # Print boards
            target_board = player_board if human_playing else computer_board
            target_board[guess_row][guess_col] = "X" if (result == 1) or\
                (result == -1) else "-"
            print_board(
                name if human_playing else COMPUTER_NAME, target_board)

            guess_msg = "You" if human_playing else COMPUTER_NAME
            print(f"{guess_msg} guessed ({guess_row},{guess_col})")
            if result == 0:
                print(f"{guess_msg} missed!\n")
            elif result == 1:
                print("\nComputer hit your battleship!\n")
                game_over = True
            else:
                print("You hit the battleship!")
                print("\nWell done! You Win! \n")
                game_over = True
            human_playing = not human_playing

        # Restart the game or not
        print("Game Over, would you like to play again or close the game?")
        restart = input("Enter 'Y' to restart or any other key to quit\n")

        if restart.capitalize() != "Y":
            break


main()
