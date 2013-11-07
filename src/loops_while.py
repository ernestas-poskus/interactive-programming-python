count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1
	
	
	
	
	
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    count += 1
    if num == 5:
        print "Sorry, you lose!"
        break
else:
    print "You win!"
	
	
	
	
	
	
	
from random import randrange

random_number = randrange(1, 10)

count = 0
# Start your game!
while count < 3:
    guess = int(raw_input("Enter a guess:"))
    num = random.randint(1, 6)
    count += 1
    if guess == random_number:
        print 'You win!'
        break
else:
    print 'You lose.'