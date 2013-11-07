hobbies = []

# Add your code below!
for i in range(0,3):
    user_hobbie = raw_input("What's your hobbie ?")
    hobbies.append(user_hobbie)
	
	
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for c in word:
    print c
	
	
#####################################################################################################################################
	
	
s = "A bird in the hand..."

# Add your for loop
for char in s:
    if (char != 'A' and char != 'a'):
        print char,
    else:
        print 'X',




#Don't delete this print statement!
print


#####################################################################################################################################


numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

# Add your loop below!
for num in numbers:
    print num ** 2


#####################################################################################################################################
	
	
d = {'x': 9, 'y': 10, 'z': 20}

for key in d:
    print str(key) + ' ' + str(d[key])
    	
		
		
#####################################################################################################################################
		
		
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item


#####################################################################################################################################


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a < b:
        print b
    else:
        print a	
		
#####################################################################################################################################
		
		
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
	
	
#####################################################################################################################################
	
	
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
        print 'A', f
    else:
        print 'A fine selection of fruits!'	