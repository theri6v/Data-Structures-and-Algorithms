# Python 3 program to find 
# factorial of given number 

# Function to find factorial of given number 
def factorial(n): 
	
	if n == 0: 
		return 1
	
	return n * factorial(n-1) 

# Driver Code 
num = 5; 
print("Factorial of", num, "is", 
factorial(num)) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Iterative Solution to find factorial of a number:
Factorial can also be calculated iteratively as recursion can be costly for large numbers. Here we have shown the iterative approach using both for and while loops. 

Approach 1: Using For loop 

Follow the steps to solve the problem:

Using a for loop, we will write a program for finding the factorial of a number. 
An integer variable with a value of 1 will be used in the program. 
With each iteration, the value will increase by 1 until it equals the value entered by the user. 
The factorial of the number entered by the user will be the final value in the fact variable.
Below is the implementation for the above approach:


# Python 3 program to find 
# factorial of given number 

# Function to find factorial of given number 
def factorial(n): 
	
	res = 1
	
	for i in range(2, n+1): 
		res *= i 
	return res 

# Driver Code 
num = 5; 
print("Factorial of", num, "is", 
factorial(num)) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Approach 2: This example uses a while loop to implement the algorithm and find the factorial program.


  # Python 3 program to find 
# factorial of given number 

# Function to find factorial of given number 
def factorial(n): 
	if(n == 0): 
	return 1
	i = n 
	fact = 1
	
	while(n / i != n): 
		fact = fact * i 
		i -= 1
		
	return fact 

# Driver Code 
num = 5; 
print("Factorial of", num, "is", 
factorial(num)) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Approach 3: A ternary operator can be thought of as a shorthand for an if…else statement. 
The conditions are provided, along with statements to be executed based on them. 
Here’s the program for factorial using a ternary operator.

# Python 3 program to find 
# factorial of given number 

def factorial(n): 

	# single line to find factorial 
	return 1 if (n == 1 or n == 0) else n * factorial(n - 1) 


# Driver Code 
num = 5
print ("Factorial of", num, "is", 
	factorial(num)) 





