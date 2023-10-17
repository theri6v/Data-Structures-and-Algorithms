
# Python3 program to find maximum 
# achievable value with a knapsack 
# of weight W and multiple instances allowed. 

# Returns the maximum value 
# with knapsack of W capacity 
def unboundedKnapsack(W, n, val, wt): 

	# dp[i] is going to store maximum 
	# value with knapsack capacity i. 
	dp = [0 for i in range(W + 1)] 

	ans = 0

	# Fill dp[] using above recursive formula 
	for i in range(W + 1): 
		for j in range(n): 
			if (wt[j] <= i): 
				dp[i] = max(dp[i], dp[i - wt[j]] + val[j]) 

	return dp[W] 

# Driver program 
W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 

print(unboundedKnapsack(W, n, val, wt)) 

-------------------------------------------------------------------------------------
#Memoization:  Like other typical Dynamic Programming(DP) problems, 
#re-computation of same subproblems can be avoided by constructing a temporary array K[][] in bottom-up manner. 
#Following is Dynamic Programming based implementation.

def unboundedKnapsack(W, wt, val, idx, dp): 
	# Base Case 
	# if we are at idx 0. 
	if idx == 0: 
		return (W // wt[0]) * val[0] 
	# If the value is already calculated then we will 
	# previous calculated value 
	if dp[idx][W] != -1: 
		return dp[idx][W] 
	# There are two cases either take element or not take. 
	# If not take then 
	notTake = 0 + unboundedKnapsack(W, wt, val, idx - 1, dp) 
	# if take then weight = W-wt[idx] and index will remain 
	# same. 
	take = float('-inf') 
	if wt[idx] <= W: 
		take = val[idx] + unboundedKnapsack(W - wt[idx], wt, val, idx, dp) 
	dp[idx][W] = max(take, notTake) 
	return dp[idx][W] 

# Driver code 
W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 
dp = [[-1 for _ in range(W+1)] for _ in range(n)] 
print(unboundedKnapsack(W, wt, val, n-1, dp)) 

	

