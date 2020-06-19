# Tic Tac Toe game in python

# global variables

# Tic tac toe board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# game going check
game_still_going = True

# default current player
current_player = "X"

# default winner
winner = None


# function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# function to play the game
def play_game():
    display_board()
    # for the game to move on
    while game_still_going:

        handle_player(current_player)

        check_game_over()

        flip_turn()

    if winner == 'X' or winner == 'O':
        print(winner + ' won')
    else:
        print("It's a tie")


# function to handle the user
def handle_player(player):
    print(player + "'s turn")
    position = input("Enter a position from 1 - 9: ")

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Wrong position entered")
            position = input("Enter a position from 1 - 9: ")

        position = int(position)-1
        if board[position] == '-':
            valid = True
        else:
            print("You can't go there")
    board[position] = player
    display_board()


# function to check whether the game is over or not
def check_game_over():
    # check winner
    check_for_winner()
    # check draw
    check_for_draw()


# function to check for winner
def check_for_winner():
    # declaring global variable
    global winner
    # check for row winner
    row_winner = check_row_winner()
    # check for column winner
    column_winner = check_column_winner()
    # check for diagonal winner
    diagonal_winner = check_diagonal_winner()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner


# function to check for row winner
def check_row_winner():
    # declaring global variable
    global game_still_going
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    if row1 or row2 or row3:
        game_still_going = False

    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]


# function to check for column winner
def check_column_winner():
    # declaring global variable
    global game_still_going
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    if column1 or column2 or column3:
        game_still_going = False

    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]


# function to check for diagonal winner
def check_diagonal_winner():
    # declaring global variable
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'

    if diagonal1 or diagonal2:
        game_still_going = False

    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]


# function to check whether the game is draw or not
def check_for_draw():
    global game_still_going
    if '-' not in board:
        game_still_going = False


# function to flip the turn of the player
def flip_turn():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
# Requirements

# 1. Display board
# 2. Place X and O in the board
# 3. Announce the winner

