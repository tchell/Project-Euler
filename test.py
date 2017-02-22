
import math

def main():
	number_list = [1, 2, 3, 4, 5, 6]
	for index in range(len(number_list)):
		# print(index , number_list)

		check = number_list[index]

		largest = False
		if not largest:
			largest = check

		elif check > largest:
			largest = check

	print(largest)
main()
