import ps0

which = raw_input("Which function would you like to run? Type the number of the function you'd like to run.")

# 0
number = int(raw_input("Give me a number."))
even = ps0.is_even(number)
print(even)



	
#2
number = str(raw_input("Give me a number."))
sum = ps0.sum_digits(number)
print(sum)