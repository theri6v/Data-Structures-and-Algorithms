# Python3 program for activity selection problem.

# The following implementation assumes that the activities
# are already sorted according to their finish time

# Prints a maximum set of activities that can be done 
# by a single person, one at a time
def printMaxActivities(s, f):
	n = len(f)
	print("Following activities are selected")

	# The first activity is always selected
	i = 0
	print(i, end=' ')

	# Consider rest of the activities
	for j in range(1, n):

		# If this activity has start time greater than
		# or equal to the finish time of previously
		# selected activity, then select it
		if s[j] >= f[i]:
			print(j, end=' ')
			i = j


# Driver code
if __name__ == '__main__':
	s = [1, 3, 0, 5, 8, 5]
	f = [2, 4, 6, 7, 9, 9]

	# Function call
	printMaxActivities(s, f)

