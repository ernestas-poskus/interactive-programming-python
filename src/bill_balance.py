def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def get_min(balance, rate):
    return balance * rate
    
def add_monthly_interest(balance):
    return balance + ((balance * 0.15)/12)
    
    
print get_min(bill, 0.02)




##############################################



def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
	x = balance - payment
	return add_monthly_interest(x)
	
new_bill = make_payment(bill / 2, bill)
print make_payment(100, new_bill)   
    
