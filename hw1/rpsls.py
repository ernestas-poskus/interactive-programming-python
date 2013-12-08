# Mini-project 1 - Rock-paper-scissors-lizard-Spock template
#
# Ernestas Poskus

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if number == 0: 
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'

    
def name_to_number(name):
    if name == 'rock': 
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4


def rpsls(player_guess): 
    # fill in your code below
    # convert name to player_number using name_to_number
    player = name_to_number(player_guess)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player - comp_number) % 5
    
    # use if/elif/else to determine winner
    if difference == 3 or difference == 4:
        result = "Computer wins!"
    elif difference == 2 or difference == 1:
        result = "Player wins!"
    else:
        result  = "Player and computer tie!"
    
    # convert comp_number to name using number_to_name
    comp_guess = number_to_name(comp_number)
    
    # print results
    print "Player chooses", player_guess 
    print "Computer chooses",comp_guess
    print result
    print ""
    
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

