# Python3 code to find the number of 
# integral points lying on the line 
# joining the two given points

# Class to represent an Integral point 
# on XY plane.
class Point:
	
	def __init__(self, a, b):
		self.x = a
		self.y = b

# Utility function to find GCD
# of two numbers GCD of a and b
def gcd(a, b):

	if b == 0:
		return a
	return gcd(b, a % b)

# Finds the no. of Integral points
# between two given points.
def getCount(p, q):

	# If line joining p and q is parallel 
	# to x axis, then count is difference
	# of y values
	if p.x == q.x:
		return abs(p.y - q.y) - 1

	# If line joining p and q is parallel 
	# to y axis, then count is difference 
	# of x values
	if p.y == q.y:
		return abs(p.x - q.x) - 1

	return gcd(abs(p.x - q.x), 
			abs(p.y - q.y)) - 1

# Driver Code
if __name__ == "__main__":

	p = Point(1, 9)
	q = Point(8, 16)

	print("The number of integral points", 
		"between ({}, {}) and ({}, {}) is {}" . 
		format(p.x, p.y, q.x, q.y, getCount(p, q)))

