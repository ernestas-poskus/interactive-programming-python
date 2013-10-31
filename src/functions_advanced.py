def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print "With tax: %f" % bill
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print "With tip: %f" % bill
    return bill
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)




def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!




def cube(number):
    return number ** 3
    
    
def by_three(arg):
    if arg % 3 == 0:
        return cube(arg)
    else:
        return False;

by_three(9)
by_three(4)






def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)








def shut_down(c):
    arg = str(c.lower())
    if arg == 'yes':
        return "Shutting down..."
    elif arg == 'no':
        return "Shutdown aborted!"
    else:
        return "Sorry, I didn't understand you."
        
		
		
def distance_from_zero(c):
    ct = type(c)
    if ct == int or ct == float:
        return abs(c)
    else:
        return "Not an integer or float!"
		
		
		
		
		
def hotel_cost(n):
    return n * 140
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == 'Tampa':
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 'No such city'
        
def rental_car_cost(d):
    total = d * 40
    if d >= 7:
        return total - 50
    elif d >= 3:
        return total - 20
    else:
        return total

def trip_cost(c,d, spending):
    return spending + hotel_cost(d) + plane_ride_cost(c) + rental_car_cost(d)
    
print trip_cost('Los Angeles',5, 600)