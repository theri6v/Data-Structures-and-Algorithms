# Python3 program to find the 
# gray sequence of n bits. 

""" we have 2 choices for each of the n bits 
either we can include i.e invert the bit or 
we can exclude the bit i.e we can leave 
the number as it is. """
def grayCodeUtil(res, n, num):
	
	# base case when we run out bits to process
	# we simply include it in gray code sequence. 
	if (n == 0):
		res.append(num[0])
		return
		
	# ignore the bit.
	grayCodeUtil(res, n - 1, num)
	
	# invert the bit. 
	num[0] = num[0] ^ (1 << (n - 1)) 
	grayCodeUtil(res, n - 1, num) 
	
# returns the vector containing the gray
# code sequence of n bits. 
def grayCodes(n):
	res = []
	
	# num is passed by reference to keep 
	# track of current code. 
	num = [0]
	grayCodeUtil(res, n, num) 
	return res 

# Driver Code
n = 3
code = grayCodes(n) 
for i in range(len(code)):
	print(code[i])

# This code is contributed by SHUBHAMSINGH10
