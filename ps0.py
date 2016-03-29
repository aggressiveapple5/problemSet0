#0
def is_even(number):
	''' Takes user input and returns True if number is even and False if odd'''
	while number > 1:
		number -= 2
	if number == 1:
		even = False
	else:
		even = True
	return(even)

#1
def number_digits(number):
	'''Takes a non-negative number as input and returns the number of digits in the number'''
	for digit in number:
		digits.append(digit)
	length = len(digits)
	return length
#2
def sum_digits(number):
	'''Takes a non-negative number and adds its digits together'''
	digits = []
	for digit in number:
		digits.append(digit)
	sum = 0
	for digit in digits:
		sum += int(digit)
	return sum