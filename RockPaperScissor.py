import random
# Rock Scissor Paper game

# global variables

# dictionary to store game items
game_items = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors',
    'Q': 'Quit',
}

game_item_numbers = ['R', 'P', 'S']

# default game status
game_still_going = True

# default player choice
player_choice = None

# default computer choice
computer_choice = None

# default scores
player_score = 0
computer_score = 0


# function to play the game
def play_game():

    print('''
    Game instructions:
    R -> Rock
    P -> Paper
    S -> Scissors
    Q -> Quit
    ''')

    while game_still_going:
        # ask user choice
        get_player_choice()
        # get computer choice
        get_computer_choice()
        # find winner
        find_winner()
        # function to display score
        display_score()


# function to get player choice
def get_player_choice():
    # declaring global variables
    global player_choice
    player_choice = input("Rock(R) / Paper(P) / Scissor(S): ").upper()
    while player_choice not in ['R', 'P', 'S', 'Q']:
        print("You have entered incorrect input")
        print("Give R -> Rock, P -> Paper, S -> Scissor, Q -> To quit\n")
        player_choice = input("Rock(R) / Paper(P) / Scissor(S): ").upper()

    player_choice = game_items.get(player_choice)
    quit_game()
    if game_still_going == False:
        exit()
    print(f"Player choice : {player_choice}")
    return player_choice


# function to get computer choice
def get_computer_choice():
    # declaring global variables
    global computer_choice
    computer_choice = random.choice(game_item_numbers)
    computer_choice = game_items.get(computer_choice)
    print(f"Computer Choice: {computer_choice}")
    return computer_choice


# function to find the winner
def find_winner():
    # declaring global variables
    global player_score, computer_score
    if player_choice == 'Rock' and computer_choice == 'Paper':
        computer_score = computer_score + 1
        print("Computer won\n")
    elif player_choice == 'Rock' and computer_choice == 'Scissors':
        player_score = player_score + 1
        print("You won\n")
    elif player_choice == 'Paper' and computer_choice == 'Rock':
        player_score = player_score + 1
        print("You won\n")
    elif player_choice == 'Paper' and computer_choice == 'Scissors':
        computer_score = computer_score + 1
        print("Computer won\n")
    elif player_choice == 'Scissors' and computer_choice == 'Rock':
        computer_score = computer_score + 1
        print("Computer won\n")
    elif player_choice == 'Scissors' and computer_choice == 'Paper':
        player_score = player_score + 1
        print("You won\n")
    else:
        print("It's a draw\n")
    return player_score, computer_score


# function to display the score
def display_score():
    global player_score, computer_score
    print(f"Your Score: {player_score}")
    print(f"Computer Score: {computer_score}\n")


# function to quit the game and display the winner
def quit_game():
    global game_still_going, player_choice, computer_score, player_score
    if player_choice == 'Quit':
        game_still_going = False
        if player_score > computer_score:
            print("You won the match")
        elif computer_score > player_score:
            print("Computer won the match")
        else:
            print("Nobody won the match")

play_game()


# Requirements
# Player1 choice
# Computer choice
# compare both
# Return winner
# add points
# end game

