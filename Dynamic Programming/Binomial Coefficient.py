'''A naive recursive Python implementation'''


def binomialCoeff(n, k):

	if k > n:
		return 0
	if k == 0 or k == n:
		return 1

	# Recursive Call
	return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)


# Driver Program to test ht above function
n = 5
k = 2
print ("Value of C(%d,%d) is (%d)" % (n, k,
									binomialCoeff(n, k)))


'''A Dynamic Programming based Python Program that uses table C[][] to calculate the Binomial Coefficient'''

# Returns value of Binomial Coefficient C(n, k)


def binomialCoef(n, k):
	C = [[0 for x in range(k+1)] for x in range(n+1)]

	# Calculate value of Binomial
	# Coefficient in bottom up manner
	for i in range(n+1):
		for j in range(min(i, k)+1):
			# Base Cases
			if j == 0 or j == i:
				C[i][j] = 1

			# Calculate value using
			# previously stored values
			else:
				C[i][j] = C[i-1][j-1] + C[i-1][j]

	return C[n][k]


# Driver program to test above function
n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
	+ str(binomialCoef(n, k)))

'''Python program for Optimized Dynamic Programming solution to Binomial Coefficient. This one uses the concept of pascal Triangle and less memory'''


def binomialCoeff(n, k):

	# Declaring an empty array
	C = [0 for i in range(k+1)]
	C[0] = 1 # since nC0 is 1

	for i in range(1, n+1):

		# Compute next row of pascal triangle using
		# the previous row
		j = min(i, k)
		while (j > 0):
			C[j] = C[j] + C[j-1]
			j -= 1

	return C[k]


# Driver Code
n = 5
k = 2
print ("Value of C(%d,%d) is %d" % (n, k, binomialCoeff(n, k)))



'''A Dynamic Programming based solution that uses table dp[][] to calculate the Binomial Coefficient. A naive recursive approach with table Python3 implementation'''

# Returns value of Binomial 
# Coefficient C(n, k) 
def binomialCoeffUtil(n, k, dp):
	
	# If value in lookup table then return 
	if dp[n][k] != -1: 
		return dp[n][k] 

	# Store value in a table before return 
	if k == 0:
		dp[n][k] = 1
		return dp[n][k] 
	
	# Store value in table before return 
	if k == n: 
		dp[n][k] = 1
		return dp[n][k] 
	
	# Save value in lookup table before return 
	dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
				binomialCoeffUtil(n - 1, k, dp))
				
	return dp[n][k] 

def binomialCoeff(n, k):
	
	# Make a temporary lookup table 
	dp = [ [ -1 for y in range(k + 1) ] 
				for x in range(n + 1) ] 

	return binomialCoeffUtil(n, k, dp)

# Driver code
n = 5
k = 2

print("Value of C(" + str(n) +
			", " + str(k) + ") is",
			binomialCoeff(n, k)) 


#Cancellation of factors between numerator and denominator:

import math
class GFG:
	def nCr(self, n, r):
		def gcd(a,b): # function to find gcd of two numbers in O(log(min(a,b)))
			if b==0: # base case
				return a
			return gcd(b,a%b)
		if r>n:
			return 0
		if r>n-r: # C(n,r) = C(n,n-r) better time complexity for lesser r value
			r = n-r
		mod = 10**9 + 7
		arr = list(range(n-r+1,n+1)) # array of elements from n-r+1 to n
		ans = 1
		for i in range(1,r+1): # for numbers from 1 to r find arr[j] such that gcd(i,arr[j])>1
			j=0
			while j<len(arr):
				x = gcd(i,arr[j])
				if x>1:
					arr[j] //= x # if gcd>1, divide both by gcd
					i //= x
				if arr[j]==1: # if element becomes 1, its of no use anymore so delete from arr
					del arr[j]
					j -= 1
				if i==1:
					break # if i becomes 1, no need to search arr
				j += 1
		for i in arr: # single pass to multiply the numerator
			ans = (ans*i)%mod
		return ans
	# Driver code
n = 5
k = 2
ob = GFG()
print("Value of C(" + str(n) +
			", " + str(k) + ") is",
			ob.nCr(n, k))

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Python code for the above approach
import math

class GFG:
	def nCr(self, n, r):
	
		# Base case
		if r > n: 
			return 0
		
		# C(n,r) = C(n,n-r) Complexity for this 
		# code is lesser for lower n-r
		if n - r > r: 
			r = n - r
			
		# List to store smallest prime factor 
		# of every number from 1 to n
		SPF = [i for i in range(n+1)]
		for i in range(4, n+1, 2):
		
			# set smallest prime factor of 
			# all even numbers as 2
			SPF[i] = 2
	
		for i in range(3, n+1, 2): 
		
			if i*i > n:
				break
			
			# Check if i is prime
			if SPF[i] == i: 
				
				# All multiples of i are composite 
				# (and divisible by i) so add i to 
				# their prime factorization getpow(j,i) times
				for j in range(i*i, n+1, i):
					if SPF[j] == j:
					
						# set smallest prime factor 
						# of j to i only if it is 
						# not previously set
						SPF[j] = i
		
		# dictionary to store power of each prime in C(n,r)
		prime_pow = {} 
		
		# For numerator count frequency 
		# of each prime factor
		for i in range(r+1, n+1):
			t = i
			
			# Recursive division to 
			# find prime factorization of i
			while t > 1: 
				if not SPF[t] in prime_pow:
					prime_pow[SPF[t]] = 1
				else:
					prime_pow[SPF[t]] += 1
				t //= SPF[t]
		
		# For denominator subtract the 
		# power of each prime factor
		for i in range(1, n-r+1): 
			t = i
			
			# Recursive division to
			# find prime factorization of i
			while t > 1: 
				prime_pow[SPF[t]] -= 1
				t //= SPF[t]
		ans = 1
		mod = 10**9 + 7
		
		# Use (a*b)%mod = (a%mod * b%mod)%mod
		for i in prime_pow: 
		
			# pow(base,exp,mod) is used to 
			# find (base^exp)%mod fast
			ans = (ans*pow(i, prime_pow[i], mod)) % mod
		return ans


# Driver code
n = 5
k = 2
ob = GFG()
print("Value of C(" + str(n) +
	", " + str(k) + ") is",
	ob.nCr(n, k))

-------------------------------------------------------------------------------------------------------------------------------------------------
# Python3 program for the above approach

# Function to find binomial
# coefficient
def binomialCoeff(n, r):
	
	if (r > n):
		return 0
		
	m = 1000000007
	inv = [0 for i in range(r + 1)]
	inv[0] = 1
	if(r+1>=2):
		inv[1] = 1

	# Getting the modular inversion
	# for all the numbers
	# from 2 to r with respect to m
	# here m = 1000000007
	for i in range(2, r + 1):
		inv[i] = m - (m // i) * inv[m % i] % m

	ans = 1

	# for 1/(r!) part
	for i in range(2, r + 1):
		ans = ((ans % m) * (inv[i] % m)) % m

	# for (n)*(n-1)*(n-2)*...*(n-r+1) part
	for i in range(n, n - r, -1):
		ans = ((ans % m) * (i % m)) % m
		
	return ans

# Driver code
n = 5
r = 2

print("Value of C(",n , "," , r ,") is ",binomialCoeff(n, r))









