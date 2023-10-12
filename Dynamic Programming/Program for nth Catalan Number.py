'''A recursive function to find nth catalan number'''


def catalan(n):
	# Base Case
	if n <= 1:
		return 1

	# Catalan(n) is the sum
	# of catalan(i)*catalan(n-i-1)
	res = 0
	for i in range(n):
		res += catalan(i) * catalan(n-i-1)

	return res


# Driver Code
for i in range(10):
	print(catalan(i), end=" ")


'''Dynamic Programming Solution for Catalan number'''
# A dynamic programming based function to find nth
# Catalan number


def catalan(n):
	if (n == 0 or n == 1):
		return 1

	# Table to store results of subproblems
	catalan = [0]*(n+1)

	# Initialize first two values in table
	catalan[0] = 1
	catalan[1] = 1

	# Fill entries in catalan[]
	# using recursive formula
	for i in range(2, n + 1):
		for j in range(i):
			catalan[i] += catalan[j] * catalan[i-j-1]

	# Return last entry
	return catalan[n]


# Driver code
for i in range(10):
	print(catalan(i), end=" ")


'''Binomial Coefficient  Solution for Catalan number'''

# Python program for nth Catalan Number
# Returns value of Binomial Coefficient C(n, k)


def binomialCoefficient(n, k):

	# since C(n, k) = C(n, n - k)
	if (k > n - k):
		k = n - k

	# initialize result
	res = 1

	# Calculate value of [n * (n-1) *---* (n-k + 1)]
	# / [k * (k-1) *----* 1]
	for i in range(k):
		res = res * (n - i)
		res = res / (i + 1)
	return res

# A Binomial coefficient based function to
# find nth catalan number in O(n) time


def catalan(n):
	c = binomialCoefficient(2*n, n)
	return c/(n + 1)


# Driver Code
for i in range(10):
	print(catalan(i), end=" ")


'''Catalan number using the multi-Precision library'''
# Function to print the number
def catalan(n):

	cat_ = 1

	# For the first number
	print(cat_, " ", end='') # C(0)

	# Iterate till N
	for i in range(1, n):

		# Calculate the number
		# and print it
		cat_ *= (4 * i - 2)
		cat_ //= (i + 1)
		print(cat_, " ", end='')


# Driver code
n = 5

# Function call
catalan(n)


'''Catalan number using BigInteger'''

def findCatalan(n):
	b = 1

	# calculating n!
	for i in range(1, n + 1, 1):
		b = b * i

	# calculating n! * n!
	b = b * b
	d = 1

	# calculating (2n)!
	for i in range(1, 2 * n + 1, 1):
		d = d * i
		
	# calculating (2n)! / (n! * n!)
	ans = d / b
	
	# calculating (2n)! / ((n! * n!) * (n+1))
	ans = ans / (n + 1)

	return ans

# Driver Code
n = 50
print(int(findCatalan(n)))





