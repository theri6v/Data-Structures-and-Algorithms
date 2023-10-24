'''Python program to find point that divides given line in given ratio.'''

def section(x1, x2, y1, y2, m, n):

	# Applying section formula
	x = (float)((n * x1)+(m * x2))/(m + n)
	y = (float)((n * y1)+(m * y2))/(m + n)

	# Printing result
	print (x, y)

x1 = 2
x2 = 4
y1 = 4
y2 = 6
m = 2
n = 3
section(x1, x2, y1, y2, m, n)
