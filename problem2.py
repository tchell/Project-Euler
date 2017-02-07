# Euler Problem 2: Even Fibonacci Numbers
# This program calculates the even and then finds the sum of all 
# Fibonacci numbers up to 4 million

import math

def main():
	
	even_fibonacci = []
	n = 0
	x = 0	
	
	while x < 4000000:
		x = fibonacci(n)
		if x >= 4000000:
			break
		even_fibonacci.append(x)
		n = n + 3
		
	print(sum(even_fibonacci))
		
def fibonacci(n):
	# Calculates the corresponding fibonacci number from the given nth value returns the
	# value of the number calculated.
	# -n is the 'number' in the fibonacci series that is being calculated

	gratio = 1.61803398875
	
	x = (math.pow(gratio, int(n)) - math.pow((1 - gratio), int(n))) / math.sqrt(5)
	
	x = round(x)
	
	return x
	
main()
