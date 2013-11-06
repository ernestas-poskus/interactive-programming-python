start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    n = number ** 2
    square_list.append(n)
    
square_list.sort()

print square_list





webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for k in webster:
    print webster[k]
	
	
	
	
	
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


for even in a:
    if even % 2 == 0:
        print even
  
  
  
  
  
# Write your function below!
def fizz_count(fizz_list):
    count = 0
    for item in fizz_list:
        if item == 'fizz':
            count += 1
    return count