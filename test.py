
import math

def main():
	
	n = input('n = ')
	gratio = 1.61803398875
	
	x = (math.pow(gratio, int(n)) - math.pow((1 - gratio), int(n))) / math.sqrt(5)
	
	x = round(x)
	
	print(x)
main()