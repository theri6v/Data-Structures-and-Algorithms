# Python3 program to find perimeter of area 
# covered by 1 in 2D matrix consists of 0's and 1's.

R = 3
C = 5

# Find the number of covered side for mat[i][j].
def numofneighbour(mat, i, j):

	count = 0;

	# UP
	if (i > 0 and mat[i - 1][j]):
		count+= 1;

	# LEFT
	if (j > 0 and mat[i][j - 1]):
		count+= 1;

	# DOWN
	if (i < R-1 and mat[i + 1][j]):
		count+= 1

	# RIGHT
	if (j < C-1 and mat[i][j + 1]):
		count+= 1;

	return count;

# Returns sum of perimeter of shapes formed with 1s
def findperimeter(mat):

	perimeter = 0;

	# Traversing the matrix and finding ones to
	# calculate their contribution.
	for i in range(0, R):
		for j in range(0, C):
			if (mat[i][j]):
				perimeter += (4 - numofneighbour(mat, i, j));

	return perimeter;

# Driver Code
mat = [ [0, 1, 0, 0, 0],
		[1, 1, 1, 0, 0],
		[1, 0, 0, 0, 0] ]

print(findperimeter(mat), end="\n");


