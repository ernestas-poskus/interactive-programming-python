prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}



for item in stock:
    print item
    print 'price: ' + str(prices[item])
    print 'stock: ' + str(stock[item])
	
	
	


total = 0

for item in stock:
    total += stock[item] * prices[item]

print total