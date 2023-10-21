Following are the common definitions of Binomial Coefficients. 

A binomial coefficient C(n, k) can be defined as the coefficient of Xk in the expansion of (1 + X)n.
A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can be chosen from among n objects; more formally, the number of k-element subsets (or k-combinations) of an n-element set.
Given two numbers N and r, The task is to find the value of NCr 

Examples : 

Input: N = 5, r = 2
Output: 10 
Explanation: The value of 5C2 is 10


Input: N = 3, r = 1
Output: 3

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Approach: Below is the idea to solve the problem:

The total number of ways for selecting r elements out of n options are nCr = (n!) / (r! * (n-r)!) 
where n! = 1 * 2 * . . . * n.

Below is the Implementation of the above approach:


'''Python 3 program To calculate The Value Of nCr'''

def nCr(n, r):

	return (fact(n) / (fact(r) 
				* fact(n - r)))

# Returns factorial of n
def fact(n):
	if n == 0:
		return 1
	res = 1
	
	for i in range(2, n+1):
		res = res * i
		
	return res

# Driver code
n = 5
r = 3
print(int(nCr(n, r)))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another Approach:

The idea is to use a recursive function to calculate the value of nCr. The base cases are:

if r is greater than n, return 0 (there are no combinations possible)
if r is 0 or r is n, return 1 (there is only 1 combination possible in these cases)
For other values of n and r, the function calculates the value of nCr by adding the number of combinations possible by including the current element 
and the number of combinations possible by not including the current element.

Below is the Implementation of the above approach:
 

 def nCr(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)
 
 
print(nCr(5, 3))  # Output: 10


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

More efficient approach:

Iterative way of calculating NCR.    using binomial coefficient formula.

 n = 5
r = 2
sum = 1
 
# Calculate the value of n choose r using the binomial coefficient formula
for i in range(1, r+1):
    sum = sum * (n - r + i) / i
 
print(int(sum))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Another Approach(Using Logarithmic Formula):

Logarithmic formula for nCr is an alternative to the factorial formula that avoids computing factorials directly and 
it’s more efficient for large values of n and r. It uses the identity log(n!) = log(1) + log(2) + … + log(n) to express the numerator and 
denominator of the nCr in terms of sums of logarithms which allows to calculate the nCr using the Logarithmic operations. 
This approach is faster and very efficient.

The logarithmic formula for nCr is:
nCr = exp( log(n!) – log(r!) – log((n-r)!) )

Below is the implementation of above approach:

 import math
 
#  Calculates the binomial coefficient nCr using the logarithmic formula
def nCr(n, r):
    # If r is greater than n, return 0
    if r > n:
        return 0
     
    # If r is 0 or equal to n, return 1
    if r == 0 or n == r:
        return 1
    # Initialize the logarithmic sum to 0
    res = 0
     
    # Calculate the logarithmic sum of the numerator and denominator using loop
    for i in range(r):
        # Add the logarithm of (n-i) and subtract the logarithm of (i+1)
        res += math.log(n-i) - math.log(i+1)
    # Convert logarithmic sum back to a normal number
    return round(math.exp(res))
 
# Test case
n = 5
r = 2
print(nCr(n, r))
