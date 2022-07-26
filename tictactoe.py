import random


def print_board(board):
    """Prints out the state of the board passed to it as an argument"""
    print("   |   |")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("   |   |")


def get_player_letter():
    """Asks the first player to pick the letter they'll play with.
    Returns a list with Player1's letter as the first item and Player2's as
    the second"""
    letter = input("Would you like to be X or O? \n").upper()
    while not (letter == 'X' or letter == 'O'):
        print('Please type either X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def plays_first():
    """Randomly chooses who will play first."""
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'


def is_valid_move(board, move):
    """Returns True is the passed move is a free slot on the board."""
    return board[move] == " "


def player_move(board):
    """Get's the player's move."""
    move = input("Move: ")
    while str(move) not in '1 2 3 4 5 6 7 8 9'.split() or not is_valid_move(board, (int(move) - 1)):
        print("That move is invalid. Please select another move.")
        move = input("Move: ")
    return int(move)


def make_player_move(board, letter, move):
    """Writes player's a move onto the board."""
    board[move - 1] = letter


def wins_game(brd, lttr):
    """Checks the board for letter matches, vertically,
    horizintally or diagonally.
    Returns True if a player has won the game."""
    return (
       (brd[0] == lttr and brd[1] == lttr and brd[2] == lttr) or
       (brd[3] == lttr and brd[4] == lttr and brd[5] == lttr) or
       (brd[6] == lttr and brd[7] == lttr and brd[8] == lttr) or
       (brd[0] == lttr and brd[3] == lttr and brd[6] == lttr) or
       (brd[1] == lttr and brd[4] == lttr and brd[7] == lttr) or
       (brd[2] == lttr and brd[5] == lttr and brd[8] == lttr) or
       (brd[0] == lttr and brd[4] == lttr and brd[8] == lttr) or
       (brd[2] == lttr and brd[4] == lttr and brd[6] == lttr)
    )


def get_random_move(board, slots):
    valid_moves = []
    for slot in slots:
        if is_valid_move(board, slot):
            valid_moves.append(slot)

    if len(valid_moves) != 0:
        return random.choice(valid_moves)
    else:
        return None


def computer_move(board, computer_letter):
    move = get_random_move(board, [0, 1, 2, 3, 4, 5, 6, 7, 8])
    if move is not None:
        return move


def make_computer_move(board, letter, move):
    board[move] = letter


def is_board_full(board):
    """Returns True if every slot on the board is taken."""
    if " " not in board:
        return True
    return False


def restart_game():
    """Returns True if a player chooses to play again."""
    print("Do you want to play again? (type y for yes or any other key for no)")
    return input().lower().startswith('y')


print("Welcome to Tic Tac Toe.")
print("The board will be numbered top to bottom. Top left is Slot 1 and Bottom right is Slot 9. Middle left is Slot 4")

while True:
    game_board = [" "] * 9
    player_letter, computer_letter = get_player_letter()
    turn = plays_first()
    print("")
    print(f"The {turn} will go first.")
    game_running = True

    while game_running:
        if turn == "Player":
            print("")
            print("Your turn. Select a spot 1-9.")
            print_board(game_board)
            move = player_move(game_board)
            make_player_move(game_board, player_letter, move)

            if wins_game(game_board, player_letter):
                print_board(game_board)
                print("You win this game. Congratulations!")
                game_running = False
            else:
                if is_board_full(game_board):
                    print("The game is tied.")
                    break
                else:
                    turn = "Computer"
        else:
            move = computer_move(game_board, computer_letter)
            make_computer_move(game_board, computer_letter, move)

            if wins_game(game_board, computer_letter):
                print_board(game_board)
                print("The computer wins this game. Better luck next time.")
                game_running = False
            else:
                if is_board_full(game_board):
                    print("The game is tied.")
                    break
                else:
                    turn = "Player"
    if not restart_game():
        print("Thanks for playing. See you next time.")
        break
