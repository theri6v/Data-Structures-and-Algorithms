'''Python3 code for Dynamic Programming based solution for 0-1 Knapsack problem'''

# Prints the items which are put in a 
# knapsack of capacity W
def printknapSack(W, wt, val, n):
	K = [[0 for w in range(W + 1)]
			for i in range(n + 1)]
			
	# Build table K[][] in bottom
	# up manner
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i - 1] <= w:
				K[i][w] = max(val[i - 1] 
				+ K[i - 1][w - wt[i - 1]],
							K[i - 1][w])
			else:
				K[i][w] = K[i - 1][w]

	# stores the result of Knapsack
	res = K[n][W]
	print(res)
	
	w = W
	for i in range(n, 0, -1):
		if res <= 0:
			break
		# either the result comes from the
		# top (K[i-1][w]) or from (val[i-1]
		# + K[i-1] [w-wt[i-1]]) as in Knapsack
		# table. If it comes from the latter
		# one/ it means the item is included.
		if res == K[i - 1][w]:
			continue
		else:

			# This item is included.
			print(wt[i - 1])
			
			# Since this weight is included
			# its value is deducted
			res = res - val[i - 1]
			w = w - wt[i - 1]

# Driver code
val = [ 60, 100, 120 ]
wt = [ 10, 20, 30 ]
W = 50
n = len(val)
	
printknapSack(W, wt, val, n)

