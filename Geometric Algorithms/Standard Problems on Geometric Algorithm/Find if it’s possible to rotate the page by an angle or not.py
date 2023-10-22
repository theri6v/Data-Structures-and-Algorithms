# Python3 program to fill an
# array with frequencies.

# Function to find if it's possible
# to rotate page or not
def possibleOrNot(a1, a2, b1, b2, c1, c2):
	
	# Calculating distance b/w points
	dis1 = (pow(b1 - a1, 2) +
			pow(b2 - a2, 2))
	dis2 = (pow(c1 - b1, 2) +
			pow(c2 - b2, 2))

	# If distance is not equal
	if(dis1 != dis2):
		print("No")
		
	# If the points are in same line
	else if (b1 == ((a1 + c1) // 2.0) and
		b2 == ((a2 + c2) // 2.0)):
		print("No")
	else:
		print("Yes")

# Driver Code

# Points a, b, and c
a1, b1, c1 = 1, 2, 3
a2 = b2 = c2 = 0
possibleOrNot(a1, a2, b1, b2, c1, c2)


