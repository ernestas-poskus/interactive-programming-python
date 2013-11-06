# Slicing

# The most appropriate way to get the remainder of the string after removing the first letter is to use slicing. 
# If you have a string s, you can get the "slice" of s from i to j using s[i:j]. This gives you the characters from position i to j.

# For example, if s = "foo", then s[0:2] gives you "fo". Think about how to use this technique to get the rest of the string minus the first character.


pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]

if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
    new_word = original + pyg
else:
    new_word = word[1:] + first + 'ay'
    print new_word



	
	
	
animals = "catdogfrog"
cat =    animals[:3]
dog =    animals[3:6]
frog =   animals[6:]