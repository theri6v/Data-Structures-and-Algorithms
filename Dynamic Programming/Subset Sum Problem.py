#Subset Sum Problem using Recursion:

'''A recursive solution for subset sum problem'''


# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(set, n, sum):

	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False

	# If last element is greater than
	# sum, then ignore it
	if (set[n - 1] > sum):
		return isSubsetSum(set, n - 1, sum)

	# Else, check if sum can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	return isSubsetSum(
		set, n-1, sum) or isSubsetSum(
		set, n-1, sum-set[n-1])


# Driver code
if __name__ == '__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")


'''Subset Sum Problem using Memoization'''



# Python program for the above approach

# Taking the matrix as globally
tab = [[-1 for i in range(2000)] for j in range(2000)]


# Check if possible subset with
# given sum is possible or not
def subsetSum(a, n, sum):

	# If the sum is zero it means
	# we got our expected sum
	if (sum == 0):
		return 1

	if (n <= 0):
		return 0

	# If the value is not -1 it means it
	# already call the function
	# with the same value.
	# it will save our from the repetition.
	if (tab[n - 1][sum] != -1):
		return tab[n - 1][sum]

	# If the value of a[n-1] is
	# greater than the sum.
	# we call for the next value
	if (a[n - 1] > sum):
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum]
	else:

		# Here we do two calls because we
		# don't know which value is
		# full-fill our criteria
		# that's why we doing two calls
		tab[n - 1][sum] = subsetSum(a, n - 1, sum)
		return tab[n - 1][sum] or subsetSum(a, n - 1, sum - a[n - 1])


# Driver Code
if __name__ == '__main__':
	n = 5
	a = [1, 5, 3, 7, 4]
	sum = 12
	if (subsetSum(a, n, sum)):
		print("YES")
	else:
		print("NO")


'''Subset Sum Problem using Dynamic Programming'''



# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum


# Returns true if there is a subset of set[]
# with sum equal to given sum
def isSubsetSum(set, n, sum):

	# The value of subset[i][j] will be
	# true if there is a
	# subset of set[0..j-1] with sum equal to i
	subset = ([[False for i in range(sum + 1)]
			for i in range(n + 1)])

	# If sum is 0, then answer is true
	for i in range(n + 1):
		subset[i][0] = True

	# If sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum + 1):
		subset[0][i] = False

	# Fill the subset table in bottom up manner
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j < set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j >= set[i-1]:
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]])

	return subset[n][sum]


# Driver code
if __name__ == '__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")

'''Subset Sum Problem using Dynamic Programming with space optimization to linear'''

# Returns True if there is a subset of set[]
# with a sum equal to the given sum
def isSubsetSum(nums, n, sum):
	# Create a list to store the previous row result
	prev = [False] * (sum + 1)

	# If sum is 0, then the answer is True
	prev[0] = True

	# If sum is not 0 and the set is empty,
	# then the answer is False
	for i in range(1, n + 1):
		curr = [False] * (sum + 1)
		for j in range(1, sum + 1):
			if j < nums[i - 1]:
				curr[j] = prev[j]
			if j >= nums[i - 1]:
				curr[j] = prev[j] or prev[j - nums[i - 1]]
		# Now curr becomes prev for (i+1)-th element
		prev = curr

	return prev[sum]

# Driver code
if __name__ == "__main__":
	nums = [3, 34, 4, 12, 5, 2]
	sum_value = 9
	n = len(nums)
	if isSubsetSum(nums, n, sum_value):
		print("Found a subset with the given sum")
	else:
		print("No subset with the given sum")





