from functools import cmp_to_key
# A Python program to find simple closed path for n points
# for explanation of orientation()

# A global point needed for sorting points with reference
# to the first point. Used in compare function of qsort()
p0 = None

# A utility function to return square of distance between
# p1 and p2
def dist(p1, p2):
	return (p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])

# To find orientation of ordered triplet (p, q, r).
# The function returns following values
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
	val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

	if val == 0: return 0 # collinear
	return 1 if val > 0 else 2 # clockwise or counterclock wise

# A function used by library function qsort() to sort
# an array of points with respect to the first point
def compare(vp1, vp2):
	p1 = vp1
	p2 = vp2

	# Find orientation
	o = orientation(p0, p1, p2)
	if o == 0:
		return -1 if dist(p0, p2) >= dist(p0, p1) else 1

	return -1 if o == 2 else 1

# Prints simple closed path for a set of n points.
def printClosedPath(points, n):
	global p0
	# Find the bottommost point
	ymin = points[0][1]
	min = 0
	for i in range(1,n):
		y = points[i][1]

		# Pick the bottom-most. In case of tie, choose the
		# left most point
		if (y < ymin) or (ymin == y and points[i][0] < points[min][0]):
			ymin = points[i][1]
			min = i

	# Place the bottom-most point at first position
	temp = points[0]
	points[0] = points[min]
	points[min] = temp

	# Sort n-1 points with respect to the first point.
	# A point p1 comes before p2 in sorted output if p2
	# has larger polar angle (in counterclockwise
	# direction) than p1
	p0 = points[0]
	points.sort(key=cmp_to_key(compare))

	# Now stack has the output points, print contents
	# of stack
	for i in range(n):
		print("(",points[i][0],",",points[i][1],"), ", end="")

# Driver program to test above functions
points = [[0, 3], [1, 1], [2, 2], [4, 4], [0, 0], [1, 2], [3, 1], [3, 3]]
n = len(points)

printClosedPath(points, n)
