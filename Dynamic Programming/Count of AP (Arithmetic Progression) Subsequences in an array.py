# Python program to find number of AP 
# subsequences in the given array 

MAX = 1000001

def numofAP(a, n): 

	# initializing the minimum value and 
	# maximum value of the array. 
	minarr = +2147483647
	maxarr = -2147483648

	# Finding the minimum and 
	# maximum value of the array. 
	for i in range(n): 
		minarr = min(minarr, a[i]) 
		maxarr = max(maxarr, a[i]) 
	

	# dp[i] is going to store count of APs ending 
	# with arr[i]. 
	# sum[j] is going to store sum of all dp[]'s 
	# with j as an AP element. 
	dp = [0 for i in range(n + 1)] 
	

	# Initialize answer with n + 1 as single 
	# elements and empty array are also DP. 
	ans = n + 1

	# Traversing with all common difference. 
	for d in range((minarr - maxarr), (maxarr - minarr) + 1): 
		sum = [0 for i in range(MAX + 1)] 
		
		# Traversing all the element of the array. 
		for i in range(n): 
		
			# Initialize dp[i] = 1. 
			dp[i] = 1

			# Adding counts of APs with given differences 
			# and a[i] is last element. 
			# We consider all APs where an array element 
			# is previous element of AP with a particular 
			# difference 
			if (a[i] - d >= 1 and a[i] - d <= 1000000): 
				dp[i] += sum[a[i] - d] 

			ans += dp[i] - 1
			sum[a[i]] += dp[i] 

	return ans 

# Driver code 
arr = [ 1, 2, 3 ] 
n = len(arr) 

print(numofAP(arr, n)) 

