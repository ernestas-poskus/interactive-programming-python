# Import *just* the sqrt function from math on line 3!
from math import sqrt

sqrt(3)


# Import *everything* from the math module on line 3!
from math import *




import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!