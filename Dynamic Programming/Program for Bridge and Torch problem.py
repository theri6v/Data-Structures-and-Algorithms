# Python program to find minimum time required
# to send people on other side of bridge
dp = [[0 for x in range(2)] for y in range(1 << 20)]

# Counts set bits in a number
def countSetBits(n):

	# Using bin function in number
	ans = bin(n)
	return ans.count("1")


# Utility function to find total time required
# to send people to other side of bridge
def findMinTime(leftmask, turn, arr, n):
		# If all people has been transferred
	if(leftmask == 0):
		return 0

	res = dp[leftmask][1 if(turn == True) else 0]

	# If we already have solved this subproblem,
	# return the answer.
	if(~res != 0):
		return res

	# Calculate mask of right side of people
	rightmask = ((1 << n)-1) ^ leftmask

	# if turn == 1 means currently people are at
	# right side, thus we need to transfer
	# people to the left side
	if(turn == True):
		minRow = float('inf')
		person = 0
		for i in range(n):
				# Select one people whose time is less
			# among all others present at right
			# side
			if((rightmask & (1 << i)) != 0):
				if(minRow > arr[i]):
					person = i
					minRow = arr[i]

		# Add that person to answer and recurse for
		# next turn after initializing that person at
		# left side
		res = arr[person] + \
			findMinTime(leftmask | (1 << person), not turn, arr, n)
	else:
		# count total set bits in 'leftmask'
		if(countSetBits(leftmask) == 1):
			for i in range(n):
				# Since one person is present at left
				# side, thus return that person only
				if((leftmask & (1 << i)) != 0):
					res = arr[i]
					break
		else:
				# try for every pair of people by
			# sending them to right side

				# Initialize the result with maximum value
			res = float('inf')
			for i in range(n):
				# If ith person is not present then skip the rest loop
				if((leftmask & (1 << i)) == 0):
					continue
				for j in range(i+1, n):
					if((leftmask & (1 << j)) != 0):
						# Find maximum integer(slowest person's time)
						val = max(arr[i], arr[j])
						# Recurse for other people after un-setting the ith and jth bit of left-mask
						val += findMinTime((leftmask ^ (1 << i)
											^ (1 << j)), not turn, arr, n)
						# Find minimum answer among all chosen values
						res = min(res, val)

	return res

# Utility function to find minimum time


def findTime(arr, n):
		# Find the mask of 'n' peoples
	mask = (1 << n) - 1

	# Initialize all entries in dp as -1
	for i in range((1 << 20)):
		dp[i][0] = -1
		dp[i][1] = -1

	return findMinTime(mask, False, arr, n)


arr = [10, 20, 30]
n = 3
print(findTime(arr, n))



