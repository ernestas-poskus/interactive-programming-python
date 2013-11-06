start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    n = number ** 2
    square_list.append(n)
    
square_list.sort()

print square_list