# Python 3 program to find equable shape
# To calculate area of polygon

import math
def polygonArea(X, Y, n):
	area = 0.0

	# Calculate value of area
	# using shoelace formula
	j = n - 1
	for i in range(n):
		area += (X[j] + X[i]) * (Y[j] - Y[i])

		# j is previous vertex to i
		j = i 
	return abs(area / 2.0)

# To calculate perimeter of polygon
def polygonPerimeter(X, Y, n):
	perimeter = 0.0

	# Calculate value of perimeter
	j = n - 1
	for i in range(n):
		perimeter += math.sqrt((X[j] - X[i]) * (X[j] - X[i]) +
						(Y[j] - Y[i]) * (Y[j] - Y[i]))

		# j is previous vertex to i
		j = i 

	return perimeter

# To find equable shape
def equableShape(X, Y, n):
	# Find area and perimeter of polygon if
	# they are equal then it is equable shape
	if (polygonPerimeter(X, Y, n) == polygonArea(X, Y, n)):
		print("Equable Shape")
	else:
		print("Not Equable Shape")

# Driver program to test above function
X = [ 0, 5, 0 ]
Y = [ 0, 0, 12 ]
n = len(X)
equableShape(X, Y, n)


