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
	digits = []
	number = str(number)
	for digit in number:
		digits.append(digit)
		length = len(digits)
	return length
#2
def sum_digits(number):
	'''Takes a non-negative number and adds its digits together'''
	digits = []
	number = str(number)
	for digit in number:
		digits.append(digit)
	sum = 0
	for digit in digits:
		sum += int(digit)
	return sum
	
#3
def sum_less_ints(number):
	'''Takes a non-negative number as input and adds all the numbers less than that number.'''
	numbers = range(0 , number)
	outcome = 0
	for interger in numbers:
		outcome += interger
	return outcome
	
#4
def factorial(number):
	'''Finds the factorial of a given number.'''
	numbers = range(1 , number + 1)
	outcome = 1
	for digit in numbers:
		outcome *= digit
	return outcome

#5
def factor(x, y):
	'''Takes 2 numbers as arguments and if x is a factor of y, True will be returned. If not, then True.'''
	x = x % y
	if x == 0:
		return True
	else:
		return False
		
#6
def is_prime(number):
	'''Returns True if number is prime and False if not.'''
	list = range(2, number)
	for factor in list:
		 prime = number % factor
		 if prime == 0:
		 	return False
		 	exit()
	return True
		 	

#7
def perfect_number(number):
	'''Checks whether the number is perfect or not.'''
	list = range(1, number)
	perfectFactors = []
	for factor in list:
		 remainder = number % factor
		 if remainder == 0:
		 	perfectFactors.append(factor)
	output = 0
	for possiblePerfect in perfectFactors:
		output += possiblePerfect
	if output == number:
		return True
	else:
		return False
		 	

#8
def sum_digit_factor(number):
	'''Checks if he sum of the digits of the number divides evenly into the number then true, false otherwise.'''
	sum = sum_digits(number)
	factor = number % sum
	if factor == 0:
		return True
	else:
		return False