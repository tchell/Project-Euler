# Project Euler - Problem 3
# This program finds the largest prime factor from a given number

def main():
	number = int(input('What number would you like the largest prime factor for? '))
	prime_list = []
	prime = 2

	while True: #some boolian expression

		quotient = number / prime

		if prime >= number:
			prime_list.append(prime)
			break

		elif quotient.is_integer():
			prime_list.append(prime)
			number = quotient
			prime = 2

		else:
			prime += 1

	print(prime_list)

	largest = None
	for index in range(len(prime_list)):
		# print(index , prime_list)

		check = prime_list[index]

		if largest == None:
			largest = check

		elif check > largest:
			largest = check

	print(largest)

def factor(number, prime, prime_list):
	# Divides the current number by the current prime and checks if the
	# number is whole or not.
	# Returns the new values of number, prime and prime_list
	# - number is the current number being divided to find a prime
	# - prime is the current prime being tested
	# - prime_list is the list of succesfull primes

	quotient = number / prime
	if prime >= number:
		prime_list.append(prime)
		return [number, prime, prime_list]

	if quotient.is_integer():
		prime_list.append(prime)
		number = quotient
		prime = 2
		[number, prime, prime_list] = factor(number, prime, prime_list)

	else:
		prime += 1
		[number, prime, prime_list] = factor(number, prime, prime_list)

	return [number, prime, prime_list]

main()
