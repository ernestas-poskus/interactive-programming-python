def is_int(x):
    if int(x) == x:
        return True
    else:
        return False
	
def digit_sum(n):
    sum = 0
    for num in str(n):
        sum += int(num)
    return sum
	
	
	
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
		
		
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  
  
  
def reverse(text):
    rev = ''
    for i in range(len(text), 0, -1):
            rev += text[i-1]
    return rev
	
	
def anti_vowel(text):
    newtext=text
    for i in text:
        if i in "aeiouAEIOU":
            newtext = newtext.replace(i, "")
    return newtext
	
	
	
	
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
         
def scrabble_score(word):
    total = 0 
    for i in word:
        total += score[i.lower()]
    return total