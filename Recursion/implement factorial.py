'''Python3 code to implement factorial'''

# Factorial function
def f(n):

	# Stop condition
	if (n == 0 or n == 1):
		return 1;

	# Recursive condition
	else:
		return n * f(n - 1);


# Driver code
if __name__=='__main__':

	n = 5;
	print("factorial of",n,"is:",f(n))
	
	----------------------------------------------------------------------------------------------------------------------------------------------

def factorial(n):
	# Base case: if n is 0 or 1, return 1
	if n == 0 or n == 1:
		return 1

	# Recursive case: if n is greater than 1, call the function with n-1 and multiply by n
	else:
		return n * factorial(n-1)

# Call the factorial function and print the result
result = factorial(5)
print(result) # Output: 120

