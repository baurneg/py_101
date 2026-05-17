'''Small Rock, Paper, Scissors Game'''

import random


VALID_CHOICES = ["rock", "paper", "scissors", "spock", "lizard"]
ABBREVIATED_VALID_CHOICES = ["r", "p", "s", "sp", "l"]

def get_valid_choice(prompt):
    '''Gets valid input'''
    while True:
        user_input = input(prompt)
        if user_input.strip().lower() in ABBREVIATED_VALID_CHOICES:
            return valid_choice_selection(user_input)

        print("Not a valid choice. Please enter 'r', 'p', 's', 'sp' or 'l':  ")

def determine_winner(user_selection, computer_selection):
    '''Determines the winner based on user_input and computer selection'''
    if user_selection == computer_selection:
        return "It's a tie!"

    rules = {
            "rock": "scissors", 
            "paper": "rock",
            "scissors": "paper",
            "spock": "rock",
            "paper": "spock",
            "lizard": "paper",
            "scissors": "lizard",
            "spock": "scissors",
            "lizard": "spock",
            "rock": "lizard",
            }

    if rules[user_selection] == computer_selection:
        return "User wins!"

    return "Computer wins!"

def valid_choice_selection(prompt):
    match prompt:
        case "s":
            return "scissors"
        case "r":
            return "rock"
        case "p":
            return "paper"
        case "l":
            return "lizard"
        case "sp":
            return "spock"
computer_win_count = 0
user_win_count = 0
def count_wins(result):

    while computer_win_count <= 5 or user_win_count <= 5:
        if result == "Computer wins!":
            computer_win_count += 1
        elif result == "User wins!":
            user_win_count += 1
    return (result)
    


    
    
user_choice = get_valid_choice("Choose one, enter: \n'r' for rock \n'p' for paper \n's' for scissors \n'sp' for spock \n'l' for lizard: \n")
print(f"You played: '{user_choice.upper()}'!")

computer_choice = random.choice(VALID_CHOICES)
print(f"Computer played: '{computer_choice.upper()}'!")

RESULT = determine_winner(user_choice, computer_choice)


