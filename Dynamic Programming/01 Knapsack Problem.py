'''This is the memoization approach of 0 / 1 Knapsack in Python in simple  we can say recursion + memoization = DP'''


def knapsack(wt, val, W, n): 

	# base conditions 
	if n == 0 or W == 0: 
		return 0
	if t[n][W] != -1: 
		return t[n][W] 

	# choice diagram code 
	if wt[n-1] <= W: 
		t[n][W] = max( 
			val[n-1] + knapsack( 
				wt, val, W-wt[n-1], n-1), 
			knapsack(wt, val, W, n-1)) 
		return t[n][W] 
	elif wt[n-1] > W: 
		t[n][W] = knapsack(wt, val, W, n-1) 
		return t[n][W] 

# Driver code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	
	# We initialize the matrix with -1 at first. 
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
	print(knapsack(weight, profit, W, n)) 



#Bottom-up Approach for 0/1 Knapsack Problem:

# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem 
# Returns the maximum value that can 
# be put in a knapsack of capacity W 


def knapSack(W, wt, val, n): 
	K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

	# Build table K[][] in bottom up manner 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i-1] <= w: 
				K[i][w] = max(val[i-1] 
							+ K[i-1][w-wt[i-1]], 
							K[i-1][w]) 
			else: 
				K[i][w] = K[i-1][w] 

	return K[n][W] 


# Driver code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	print(knapSack(W, weight, profit, n)) 


#Space optimized Approach for 0/1 Knapsack Problem using Dynamic Programming:

# Python code to implement the above approach 


def knapSack(W, wt, val, n): 
	
	# Making the dp array 
	dp = [0 for i in range(W+1)] 

	# Taking first i elements 
	for i in range(1, n+1): 
		
		# Starting from back, 
		# so that we also have data of 
		# previous computation when taking i-1 items 
		for w in range(W, 0, -1): 
			if wt[i-1] <= w: 
				
				# Finding the maximum value 
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1]) 
	
	# Returning the maximum value of knapsack 
	return dp[W] 


# Driver code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	print(knapSack(W, weight, profit, n)) 




