# Problem 1 - Multiples of 3 and 5
# This program will calculate all of the multiples of 3 and 5 that are less than 1000 
# and print the sum of the multiples

def main():
	# block find 3 multiples (B)
	three_multiples = [] 
	product = 0
	multiplier = 0
	
	for product in range(0, 1000):
		
		product = 3 * multiplier
		
		if product >= 1000:
			break
			
		else:
			three_multiples.append(product)
			multiplier += 1
					
	# print(sum(three_multiples))
	
	# block find 5 multiples (B)  
	five_multiples = [] 
	product = 0
	multiplier = 0
	
	for product in range(0, 1000):
		
		product = 5 * multiplier
		
		if product >= 1000:
			break
			
		else:
			five_multiples.append(product)
			# print('5 * ' + str(multiplier) + ' = ' + str(product))
			multiplier += 1
			
	# print(sum(five_multiples))
	# block find common multiples (B)
	common_multiples = [] 
	product = 0
	multiplier = 0
	
	for product in range(0, 1000):
		
		product = 15 * multiplier
		
		if product >= 1000:
			break
			
		else:
			common_multiples.append(product)
			# print('5 * ' + str(multiplier) + ' = ' + str(product))
			multiplier += 1

	# add multiples to find sum (L)  
	# sum ← print the sum  (L)
	print(sum(three_multiples) + sum(five_multiples) - sum(common_multiples))
	
main()
