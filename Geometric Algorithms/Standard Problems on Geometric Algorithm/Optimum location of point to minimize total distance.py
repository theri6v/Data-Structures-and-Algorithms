# A Python3 program to find optimum location
# and total cost
import math

class Optimum_distance:
	
	# Class defining a point
	class Point:
		
		def __init__(self, x, y):
			
			self.x = x 
			self.y = y 
		
	# Class defining a line of ax + by + c = 0 form
	class Line:
		
		def __init__(self, a, b, c):
			
			self.a = a
			self.b = b
			self.c = c
		
	# Method to get distance of point 
	# (x, y) from point p
	def dist(self, x, y, p):
		
		return math.sqrt((x - p.x) ** 2 +
						(y - p.y) ** 2)
	
	# Utility method to compute total distance
	# all points when choose point on given
	# line has x-coordinate value as X
	def compute(self, p, n, l, x):
		
		res = 0
		
		y = -1 * (l.a*x + l.c) / l.b
		
		# Calculating Y of chosen point
		# by line equation
		for i in range(n):
			res += self.dist(x, y, p[i])
			
		return res
	
	# Utility method to find minimum total distance
	def find_Optimum_cost_untill(self, p, n, l):
		
		low = -1e6
		high = 1e6
		
		eps = 1e-6 + 1
		
		
		# Loop until difference between low
		# and high become less than EPS
		while((high - low) > eps):
		
			# mid1 and mid2 are representative x
			# co-ordiantes of search space
			mid1 = low + (high - low) / 3
			mid2 = high - (high - low) / 3
			
			dist1 = self.compute(p, n, l, mid1)
			dist2 = self.compute(p, n, l, mid2)
			
			# If mid2 point gives more total 
			# distance, skip third part
			if (dist1 < dist2):
				high = mid2
				
			# If mid1 point gives more total
			# distance, skip first part
			else:
				low = mid1
				
		# Compute optimum distance cost by 
		# sending average of low and high as X
		return self.compute(p, n, l, (low + high) / 2)
	
	# Method to find optimum cost
	def find_Optimum_cost(self, p, l):
		
		n = len(p)
		p_arr = [None] * n
		
		# Converting 2D array input to point array
		for i in range(n):
			p_obj = self.Point(p[i][0], p[i][1])
			p_arr[i] = p_obj
			
		return self.find_Optimum_cost_untill(p_arr, n, l)
	
# Driver Code
if __name__ == "__main__":
	
	obj = Optimum_distance()
	l = obj.Line(1, -1, -3)
	
	p = [ [ -3, -2 ], [ -1, 0 ], 
		[ -1, 2 ], [ 1, 2 ], 
		[ 3, 4 ] ]
	
	print(obj.find_Optimum_cost(p, l))


