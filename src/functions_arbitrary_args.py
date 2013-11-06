m = 5
n = 13
# Add add_function here!
def add_function(*args):
    total = 0 
    for n in args:
        total += n
    return total


print add_function(m, n)