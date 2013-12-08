# Mini-project 2 - "Guess the number"
#
# Ernestas Poskus

import random
import simplegui
import math


# initialize global variables used in your code
num_range = 100


# helper function to start and restart the game
def new_game():
    if num_range == 100:
        range100()
    else:
        range1000()

# helper function to inform user
def inform(_range, _guess):	
	print ""
    print "New game. Range is from 0 to "+str(_range)
    print "Number of remainin guesses is "+str(_guess)
    print ""		


# define event handlers for control panel
def range100():
    global secretNumber
    global guesses
    global num_range
    num_range = 100 # Reset back to 100
    
    guesses = math.ceil((math.log((num_range - 0)-1))/(math.log(2)))
    secretNumber = random.randrange(0,num_range)
    inform(num_range, guesses) # Write to console

def range1000():
    global secretNumber
    global guesses
    global num_range
    num_range = 1000 # Reset back to 1000
    
    guesses = math.ceil((math.log((num_range - 0)-1))/(math.log(2)))
    secretNumber = random.randrange(0,num_range)
    inform(num_range, guesses) # Write to console

    
def input_guess(guess):
    if guess != "":
        global guesses
        global secretNumber
        guesses -=1
        if secretNumber > int(guess):
            msg = "Higher!"
        elif secretNumber < int(guess):
            msg = "Lower!"
        else:
            msg = "Win!"    
        print "Guess was "+guess
        print "Number of remainin guesses is "+str(guesses)
        
        if guesses == 0 and msg != "Win!":
            msg = "You Lose!"
        
        print msg
        
        if msg == "You Lose!":
            print "The Secret number was: "+str(secretNumber)
        
        if msg == "Win!" or msg == "You Lose!":
            new_game()
    
# create frame
frame = simplegui.create_frame('Guess the number', 300, 300)
# register event handlers for control elements
frame.add_button('Range is [0,100)', range100, 200)
frame.add_button('Range is [0,1000)', range1000, 200)
frame.add_input('Enter a guess', input_guess, 50)


# call new_game and start frame
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
