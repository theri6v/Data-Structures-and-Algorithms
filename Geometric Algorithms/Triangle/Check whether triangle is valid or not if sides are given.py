'''Python3 program to check if three sides form a triangle or not'''

# function to check if three sides 
# form a triangle or not 
def checkValidity(a, b, c): 
	
	# check condition 
	if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
		return False
	else: 
		return True		

# driver code 
a = 7
b = 10
c = 5
if checkValidity(a, b, c): 
	print("Valid") 
else: 
	print("Invalid") 
