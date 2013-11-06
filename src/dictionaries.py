1.
A single dictionary can hold many types of values. The inventory dict here has both int and list values.

2.
A dictionary's keys MUST be both immutable and hashable. Don't worry if you don't understand what that means. 
In general, we only use strings, numbers or tuples as keys, but not lists, dictionaries or sets. The values can be anything you'd like.

3.
When you access a value in a dictionary you have access to that value directly. So if we have something like:


inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50