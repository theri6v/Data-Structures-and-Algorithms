Approach : Let the coordinates of four corners be A(x1, y1), B(x2, y2), C(x3, y3) and D(x4, y4). And coordinates of the given point P be (x, y)
1) Calculate area of the given rectangle, i.e., area of the rectangle ABCD as area of triangle ABC + area of triangle ACD. 
Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2 + [ x1(y4 – y3) + x4(y3 – y1) + x3(y1-y4)]/2 
2) Calculate area of the triangle PAB as A1. 
3) Calculate area of the triangle PBC as A2. 
4) Calculate area of the triangle PCD as A3. 
5) Calculate area of the triangle PAD as A4. 
6) If P lies inside the triangle, then A1 + A2 + A3 + A4 must be equal to A.


'''A utility function to calculate area of triangle formed by (x1, y1), (x2, y2) and (x3, y3)'''
def area(x1, y1, x2, y2, x3, y3):
	
	return abs((x1 * (y2 - y3) +
				x2 * (y3 - y1) +
				x3 * (y1 - y2)) / 2.0)

# A function to check whether point 
# P(x, y) lies inside the rectangle 
# formed by A(x1, y1), B(x2, y2), 
# C(x3, y3) and D(x4, y4) 
def check(x1, y1, x2, y2, x3, 
		y3, x4, y4, x, y):
			
	# Calculate area of rectangle ABCD 
	A = (area(x1, y1, x2, y2, x3, y3) +
		area(x1, y1, x4, y4, x3, y3))

	# Calculate area of triangle PAB 
	A1 = area(x, y, x1, y1, x2, y2)

	# Calculate area of triangle PBC 
	A2 = area(x, y, x2, y2, x3, y3)

	# Calculate area of triangle PCD 
	A3 = area(x, y, x3, y3, x4, y4)

	# Calculate area of triangle PAD 
	A4 = area(x, y, x1, y1, x4, y4);

	# Check if sum of A1, A2, A3 
	# and A4 is same as A 
	return (A == A1 + A2 + A3 + A4)

# Driver Code
if __name__ == '__main__':
	
	# Let us check whether the point 
	# P(10, 15) lies inside the 
	# rectangle formed by A(0, 10),
	# B(10, 0) C(0, -10) D(-10, 0) 
	if (check(0, 10, 10, 0, 0, -10, 
					-10, 0, 10, 15)):
		print("yes")
	else:
		print("no")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Approach#2: Using the Point-in-Polygon Algorithm
One way to check if a point lies inside a rectangle is to use the point-in-polygon algorithm. In this case, 
we can consider the rectangle as a polygon with four vertices, and check if the point P lies inside this polygon.

Algorithm
1. Define a function point_in_rect(rect, p) that takes the rectangle vertices rect and point p as input.
2. Use the ray casting algorithm to determine if the point p lies inside the rectangle polygon:
a. Initialize a count variable to zero
b. For each edge of the polygon, check if it intersects the ray extending from the point p to infinity in the positive x direction
c. If the edge intersects the ray, increment the count
d. If the count is odd, the point lies inside the polygon; otherwise, it lies outside


def point_in_rect(rect, p):
	n = len(rect)
	inside = False
	j = n - 1
	for i in range(n):
		if ((rect[i][1] > p[1]) != (rect[j][1] > p[1])) and \
		(p[0] < (rect[j][0] - rect[i][0]) * (p[1] - rect[i][1]) / (rect[j][1] - rect[i][1]) + rect[i][0]):
			inside = not inside
		j = i
	return inside

# Example usage
R = [(10, 10), (10, -10), (-10, -10), (-10, 10)]
P = (0, 0)
print(point_in_rect(R, P)) 

R = [(10, 10), (10, -10), (-10, -10), (-10, 10)]
P = (20, 20)
print(point_in_rect(R, P))


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------




