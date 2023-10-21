First Approach:

Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to the square root of n. While i divides n, print i, and divide n by i. After i fails to divide n, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by the above two steps. So print n if it is greater than 2.
------------------------------------------------------------------------------------------------------------------------------------------------
'''Python program to print prime factors'''

import math 

# A function to print all prime factors of 
# a given number n 
def primeFactors(n): 
	
	# Print the number of two's that divide n 
	while n % 2 == 0: 
		print 2, 
		n = n / 2
		
	# n must be odd at this point 
	# so a skip of 2 ( i = i + 2) can be used 
	for i in range(3,int(math.sqrt(n))+1,2): 
		
		# while i divides n , print i and divide n 
		while n % i== 0: 
			print i, 
			n = n / i 
			
	# Condition if n is a prime 
	# number greater than 2 
	if n > 2: 
		print n 
		
# Driver Program to test above function 

n = 315
primeFactors(n) 


