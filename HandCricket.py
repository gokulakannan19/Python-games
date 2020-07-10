import random
# Hand Cricket Game

# global variables
# default game status
game_still_going = True

# game scores_list

# toss dictionary
toss = {
    'H': 'Head',
    'T': 'Tail'
}

play_options = {
    '1': 'Bat',
    '2': 'Bowl'
}

# toss keywords
toss_keywords = ['H', 'T']

play_keywords = ['1', '2']

# default player_toss_choice
player_toss_choice = None
random_toss_choice = None

# default toss winner
toss_winner = None
# default options
decide_bat_or_bowl = None

# function to play the game
def play_game():
    # function for toss
    put_toss()
    # function to find the toss winner
    find_toss_winner()
    # function to choose bat or bowl
    bat_or_bowl()

    while game_still_going:
        pass


# function to put the toss
def put_toss():
    # declaring globsl variables
    global player_toss_choice, random_toss_choice
    print('''
    Instructions:
    H -> Head
    T -> Tail
    ''')
    player_toss_choice = input("Heads(H) or Tail(T): ").upper()
    player_toss_choice = toss.get(player_toss_choice)
    random_toss_choice = random.choice(toss_keywords)
    random_toss_choice = toss.get(random_toss_choice)
    print(f"{random_toss_choice} it is")
    return player_toss_choice, random_toss_choice


# function to find the toss winner
def find_toss_winner():
    # declaring global variable
    global toss_winner
    if player_toss_choice == random_toss_choice:
        print("Congrats! You won the toss")
        toss_winner = 'player'
    else:
        print("Sorry! you lose the toss")
        toss_winner = 'computer'

    return toss_winner


def bat_or_bowl():
    global decide_bat_or_bowl
    if toss_winner == 'player':
        decide_bat_or_bowl = input("Batting(1) or Bowling(2):")
        decide_bat_or_bowl = play_options.get(decide_bat_or_bowl)
        print(f"You choose to {decide_bat_or_bowl} first")
    else:
        decide_bat_or_bowl = random.choice(play_keywords)
        decide_bat_or_bowl = play_options.get(decide_bat_or_bowl)
        print(f"Computer choose to {decide_bat_or_bowl} first")



play_game()

# Requirements
# Put toss
# Select bat or bowl
# 1st innings
# 2nd innings
# winner
