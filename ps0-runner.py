#TODO: Let the user know what the original number is too
#Add docstrings
import ps0

which = str(raw_input("Which function would you like to run? Type the number of the function you'd like to run."))

#0
if which == "0":
	print("If 'True', then even. If 'False', then odd.")
	print("Test Case 1")
	number = 4
	print("{} is {}.".format(number, ps0.is_even(number)))
	print("Test Case 2")
	number = 7
	print("{} is {}.".format(number, ps0.is_even(number)))
	
#1
elif which == "1":
	print("Test Case 1")
	number = 0
	print("There are {} in {}.".format(ps0.number_digits(number), number))
	print("Test Case 2")
	number = 322
	print("There are {} in {}.".format(ps0.number_digits(number), number))


#2
elif which == "2":	
	print("Test Case 1")
	number = 122
	sum = ps0.sum_digits(number)
	print(sum)
	print("Test Case 2")
	number = 0
	sum = ps0.sum_digits(number)
	print(sum)
	
#3
elif which == "3":
	print("Test Case 1")
	number = 0
	print("The sum of the digits in {} is {}.".format(number, ps0.sum_less_ints(number)))
	print("Test Case 2")
	number = 12
	print("The sum of the digits in {} is {}.".format(number, ps0.sum_less_ints(number)))
	
#4
elif which == "4":
	print("Test Case 1")
	number = 0
	print("The factorial of {} is {}.".format(number, ps0.factorial(number)))
	print("Test Case 2")
	number = 4
	print("The factorial of {} is {}.".format(number, ps0.factorial(number)))
	
#5
elif which == '5':
	print("If x is a factor of y, True will be returned. If not, then True.")
	print('Test Case 1')
	x = 4
	y = 2
	print("The two numbers were {} and {}. {}.".format(x, y, ps0.factor(x, y)))
	print("Test Case 2")
	x = 5
	y = 2
	print("The two numbers were {} and {}. {}.".format(x, y, ps0.factor(x, y)))
	
	
#6
elif which == '6':
	print("If the number is prime, will return True. Otherwise, False.")
	print("Test Case 1")
	number = 11
	print("The number is {}. {}".format(number, ps0.is_prime(number)))
	print("Test Case 2")
	number = 8
	print("The number is {}. {}".format(number, ps0.is_prime(number)))
	
#7
elif which == '7':
	print("If returns True then number is perfect, else False.")
	print("Test Case 1")
	number = 6
	print("{} is {}".format(number, ps0.perfect_number(number)))
	print("Test Case 2")
	number = 11
	print("{} is {}".format(number, ps0.perfect_number(number)))
	
#8
elif which == '8':
	print("If the sym of the digits is a factor of the number, the program will return True. If not, then False.")
	print("Test Case 1")
	number = 12
	print("{} is {}.".format(number, ps0.sum_digit_factor(number)))
	print("Test Case 2")
	number = 13
	print("{} is {}.".format(number, ps0.sum_digit_factor(number)))