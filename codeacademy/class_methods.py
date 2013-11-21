# A Methodical Approach

# When a class has its own functions, those functions are called methods. 
# You've already seen one such method: __init__(). But you can also define your own methods!


class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
	def description():
	    print self.name
	    print self.age
		
		
		
##############################################################################################################
		
		
		
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = 'good'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
	
	
	
	
sloth = Animal('sloth', 22)
ocelot = Animal('ocelot', 3)

print sloth.health
print ocelot.health