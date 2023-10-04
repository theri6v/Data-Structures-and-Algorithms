 Given a sorted array of N distinct elements, find a key in the array using the least number of comparisons. (Do you think binary search is optimal to search a key in sorted array?) Without much theory, here is typical binary search algorithm. 

# Returns location of key, or -1 if not found
def BinarySearch(A, l, r, key):
	while (l < r):
		m = l + (r - l) // 2
		if A[m] == key: #first comparison
			return m
		if A[m] < key: # second comparison
			l = m + 1
		else:
			r = m - 1
	return -1

Theoretically we need log N + 1 comparisons in worst case. If we observe, we are using two comparisons per iteration except during final successful match, if any. In practice, comparison would be costly operation, it won’t be just primitive type comparison. It is more economical to minimize comparisons as that of theoretical limit. See below figure on initialize of indices in the next implementation.

# Invariant: A[l] <= key and A[r] > key
# Boundary: |r - l| = 1
# Input: A[l .... r-1]

def BinarySearch(A, l, r, key):
	while (r-l > 1):
		m = l+(r-l)//2
		if A[m] <= key:
			l = m
		else:
			r = m
	if A[l] == key:
		return l
	if A[r] == key:
		return r
	return -1

Problem Statement: Given an array of N distinct integers, find floor value of input ‘key’. Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome. We can use the above optimized implementation to find floor value of key. We keep moving the left pointer to right most as long as the invariant holds. Eventually left pointer points an element less than or equal to key (by definition floor value). The following are possible corner cases, —> If all elements in the array are smaller than key, left pointer moves till last element. —> If all elements in the array are greater than key, it is an error condition. —> If all elements in the array equal and <= key, it is worst case input to our implementation. 

Here is implementation

# largest value <= key
# Invariant: A[l] <= key and A[r] > key
# Boundary: |r - l| = 1
# Input: A[l .... r-1]
# Precondition: A[l] <= key <= A[r]
def Floor(A,l,r,key):
	while (r-l>1):
		m=l+(r-l)//2
		if A[m]<=key:
			l=m
		else:
			r=m
	return A[l]
# Initial call
def Floor(A,size,key):
	# Add error checking if key < A[0]
	if key<A[0]:
		return -1
	# Observe boundaries
	return Floor(A,0,size,key)


Problem Statement: Given a sorted array with possible duplicate elements. Find number of occurrences of input ‘key’ in log N time. The idea here is finding left and right most occurrences of key in the array using binary search. We can modify floor function to trace right most occurrence and left most occurrence. 

# Input: Indices Range [l ... r)
# Invariant: A[l] <= key and A[r] > key

def GetRightPosition(A,l,r,key):
	while r-l>1:
		m=l+(r-l)//2
		if A[m]<=key:
			l=m
		else:
			r=m
	return l
# Input: Indices Range (l ... r]
# Invariant: A[r] >= key and A[l] > key
def GetLeftPosition(A,l,r,key):
	while r-l>1:
		m=l+(r-l)//2
		if A[m]>=key:
			r=m
		else:
			l=m
	return r
def countOccurrences(A,size,key):
	#Observe boundary conditions
	left=GetLeftPosition(A,-1,size-1,key)
	right=GetRightPosition(A,0,size,key)
	# What if the element doesn't exists in the array?
	# The checks helps to trace that element exists

	if A[left]==key and key==A[right]:
		return right-left+1
	return 0


Problem Statement: Given a sorted array of distinct elements, and the array is rotated at an unknown position. Find minimum element in the array. We can see  pictorial representation of sample input array in the below figure.  

We converge the search space till l and r points single element. If the middle location falls in the first pulse, the condition A[m] < A[r] doesn’t satisfy, we converge our search space to A[m+1 … r]. If the middle location falls in the second pulse, the condition A[m] < A[r] satisfied, we converge our search space to A[1 … m]. At every iteration we check for search space size, if it is 1, we are done. 

Given below is implementation of algorithm. Can you come up with different implementation? 



def BinarySearchIndexOfMinimumRotatedArray(A, l, r):
	# extreme condition, size zero or size two
	# Precondition: A[l] > A[r]
	if A[l] >= A[r]:
		return l
	while (l <= r):
		# Termination condition (l will eventually falls on r, and r always
		# point minimum possible value)
		if l == r:
			return l
		m = l+(r-l)//2 # 'm' can fall in first pulse,
		# second pulse or exactly in the middle
		if A[m] < A[r]:
			# min can't be in the range
			# (m < i <= r), we can exclude A[m+1 ... r]
			r = m
		else:
			# min must be in the range (m < i <= r),
			# we must search in A[m+1 ... r]

			l = m+1
	return -1


def BinarySearchIndexOfMinimumRotatedArray(A, size):
	return BinarySearchIndexOfMinimumRotatedArray(A, 0, size-1)





















