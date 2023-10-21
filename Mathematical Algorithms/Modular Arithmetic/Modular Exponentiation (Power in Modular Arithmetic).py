Given three numbers x, y and p, compute (xy) % p. 

Examples : 

Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3.

Input:  x = 2, y = 5, p = 13
Output: 6
Explanation: 2^5 % 13 = 32 % 13 = 6.
We have discussed recursive and iterative solutions for power.

Below is discussed iterative solution. 


'''Iterative Function to calculate (x^y)%p in O(log y)'''

def power(x, y, p):

	# Initialize result
	res = 1

	while (y > 0):

		# If y is odd, multiply x with result
		if ((y & 1) != 0):
			res = res * x

		# y must be even now
		y = y >> 1 # y = y/2
		x = x * x # Change x to x^2

	return res % p

# Driver Code


x = 2
y = 5
p = 13
print("Power is ", power(x, y, p))

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Efficient Approach:'''

The problem with the above solutions is, overflow may occur for large values of n or x. Therefore, power is generally evaluated under the modulo of a large number.

Below is the fundamental modular property that is used for efficiently computing power under modular arithmetic. 

(ab) mod p = ( (a mod p) (b mod p) ) mod p 

For example a = 50,  b = 100, p = 13
50  mod 13  = 11
100 mod 13  = 9

(50 * 100) mod 13 = ( (50 mod 13) * (100 mod 13) ) mod 13 
or (5000) mod 13 = ( 11 * 9 ) mod 13
or 8 = 8
Below is the implementation based on the above property.  

 # Iterative Python3 program
# to compute modular power
 
# Iterative Function to calculate
# (x^y)%p in O(log y) 
def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p 
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res
     
 
# Driver Code
 
x = 2; y = 5; p = 13
print("Power is ", power(x, y, p))
