'''METHOD 1: (Using Dynamic Programming)'''

# A Dynamic Programming based solution to compute nCr % p

# Returns nCr % p
def nCrModp(n, r, p):

	# Optimization for the cases when r is large
	# compared to n-r 
	if (r > n- r):
		r = n - r 

	# The array C is going to store last row of
	# pascal triangle at the end. And last entry
	# of last row is nCr.
	C = [0 for i in range(r + 1)]

	C[0] = 1 # Top row of Pascal Triangle

	# One by constructs remaining rows of Pascal
	# Triangle from top to bottom
	for i in range(1, n + 1):

		# Fill entries of current row 
		# using previous row values
		for j in range(min(i, r), 0, -1):

			# nCj = (n - 1)Cj + (n - 1)C(j - 1)
			C[j] = (C[j] + C[j-1]) % p

	return C[r]

# Driver Program
n = 10
r = 2
p = 13
print('Value of nCr % p is', nCrModp(n, r, p))





'''Let’s find out how to build Pascal Triangle for the same'''


# Python3 program to find the nCr%p
# based on optimal Dynamic
# Programming implementation and
# Pascal Triangle concepts

# Returns (a * b) % mod
def moduloMultiplication(a, b, mod):
	# Initialize result
	res = 0

	# Update a if it is more than
	# or equal to mod
	a %= mod

	while (b):

		# If b is odd, add a with result
		if (b & 1):
			res = (res + a) % mod

		# Here we assume that doing 2*a
		# doesn't cause overflow
		a = (2 * a) % mod
		b >>= 1 # b = b / 2

	return res


# Global Variables
x, y = 0, 1

# Function for extended Euclidean Algorithm


def gcdExtended(a, b):
	global x, y

	# Base Case
	if (a == 0):

		x = 0
		y = 1
		return b

	# To store results of recursive call
	gcd = gcdExtended(b % a, a)
	x1 = x
	y1 = y

	# Update x and y using results of recursive
	# call
	x = y1 - int(b / a) * x1
	y = x1

	return gcd


def modInverse(a, m):

	g = gcdExtended(a, m)

	# Return -1 if b and m are not co-prime
	if (g != 1):
		return -1

	# m is added to handle negative x
	return (x % m + m) % m


# Function to compute a/b under modulo m
def modDivide(a, b, m):

	a = a % m
	inv = modInverse(b, m)
	if (inv == -1):
		return 0
	else:
		return (inv * a) % m


# Function to calculate nCr % p
def nCr(n, r, p):

	# Edge Case which is not possible
	if (r > n):
		return 0

	# Optimization for the cases when r is large
	if (r > n - r):
		r = n - r

	# x stores the current result at
	x = 1

	# each iteration
	# Initialized to 1 as nC0 is always 1.
	for i in range(1, r + 1):

		# Formula derived for calculating result is
		# C(n,r-1)*(n-r+1)/r
		# Function calculates x*(n-i+1) % p.
		x = moduloMultiplication(x, (n + 1 - i), p)

		# Function calculates x/i % p.
		x = modDivide(x, i, p)

	return x

# Driver Code
n = 5
r = 3
p = 1000000007
print("Value of nCr % p is ", nCr(n, r, p))

# This code is contributed by phasing17
