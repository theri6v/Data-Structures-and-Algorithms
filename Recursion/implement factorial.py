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
	
	# This code is contributed by pratham76.
