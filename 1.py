#The is_positive function should return True if the number received is positive, otherwise it returns None. 
#Can you fill in the gaps to make that happen?
def is_positive(number):
  if number>0:
    return bool(number)
    
    
------------------------------------------------------------------------------------------------------------------------------
def is_positive(number):
  if number > 0:
    return True
  else:
   return False

------------------------------------------------------------------------------------------------------------------------------
#working 
def is_even(number):
   if number % 2 == 0:
    return True 
   else:
    return False 

print(is_even(3))

------------------------------------------------------------------------------------------------------------------------------
#elif Statements

def number_group(number):
  if number>0:
    return "Positive"
  elif number<0:
    return "Negative"
  else:
   return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
----------------------------------------------------------------------------------------------------------------------------------------
#Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
#Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
-----------------------------------------------------------------------------------------------------
# while loop
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))
-------------------------------------------------------------------------------------

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

-------------------------------------------------------------------------------------------
def count_down(start_number):
  current =start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
------------------------------------------------------------------------------------------------------------------
#Fill in the blanks to make the print_prime_factors function print all the prime factors of a number. 
#A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

------------------------------------------------------

#The following code can lead to an infinite loop. Fix the code so that it can finish successfully for all numbers.

#Note: Try running your function with the number 0 as the input, and see what you get!

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n >1:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
---------------------------------------------------------------------------

#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement. 
#Fill in the blanks to complete the function to satisfy these conditions

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number
		# What is the additional condition to exit out of the loop?
		if result > 25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier+= 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

-----------------------------------------------------------------------------------------------------------------

####  for loop?   #####

#Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). 
#Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(1,x):
        sum +=square(n)
    return sum

print(sum_squares(10)) # Should be 285






def factorial(n):
    result =1
    for i in range (result,(n+1)):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

















