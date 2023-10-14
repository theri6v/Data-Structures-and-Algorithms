1) Optimal Substructure: 

'''A recursive solution for Rod cutting problem'''

# Returns the best obtainable price for a rod of length n
# and price[] as prices of different pieces 
def cutRod(price, index, n):
	
	# base case
	if index == 0:
		return n*price[0]
	
	# At any index we have 2 options either
	# cut the rod of this length or not cut 
	# it
	notCut = cutRod(price,index - 1,n)
	cut = float("-inf")
	rod_length = index + 1

	if (rod_length <= n):
		
		cut = price[index]+cutRod(price,index,n - rod_length)

	return max(notCut, cut)

# Driver program to test above functions 
arr = [ 1, 5, 8, 9, 10, 17, 17, 20 ]
size = len(arr)
print("Maximum Obtainable Value is ",cutRod(arr, size - 1, size))



2) Overlapping Subproblems:

#A memoization solution for Rod cutting problem

# Returns the best obtainable price for 
# a rod of length n and price[] as 
# prices of different pieces
def cutRoad(price,index,n,dp):

	# base case
	if(index == 0):
		return n*price[0]
	if(dp[index][n] != -1):
		return dp[index][n]
	
	# At any index we have 2 options either 
	# cut the rod of this length or not cut it
	notCut = cutRoad(price,index-1,n,dp)
	cut = -5
	rod_length = index + 1
	if(rod_length <= n):
		cut = price[index] + cutRoad(price,index,n-rod_length,dp)
	dp[index][n] = max(notCut,cut)
	return dp[index][n]

# Driver program to test above functions
if __name__ == "__main__":
	arr = [1,5,8,9,10,17,17,20]
	size = len(arr)
	dp = []
	temp = []
	for i in range(0,size+1):
		temp.append(-1)
	for i in range(0,size):
		dp.append(temp)
	# print(dp)
	print("Maximum Obtainable Value is :",end=' ')
	print(cutRoad(arr,size-1,size,dp))

-----------------------------------------------------------


# A Dynamic Programming solution for Rod cutting problem
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
	val = [0 for x in range(n+1)]
	val[0] = 0

	# Build the table val[] in bottom up manner and return
	# the last entry from the table
	for i in range(1, n+1):
		max_val = INT_MIN
		for j in range(i):
			max_val = max(max_val, price[j] + val[i-j-1])
		val[i] = max_val

	return val[n]

# Driver program to test above functions
arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))


3) Using the idea of Unbounded Knapsack.



  # Python program for above approach

# Global Array for
# the purpose of memoization.
t = [[0 for i in range(9)] for j in range(9)]

# A recursive program, using ,
# memoization, to implement the
# rod cutting problem(Top-Down).
def un_kp(price, length, Max_len, n):

	# The maximum price will be zero,
	# when either the length of the rod
	# is zero or price is zero.
	if (n == 0 or Max_len == 0):
		return 0;
	

	# If the length of the rod is less
	# than the maximum length, Max_lene will
	# consider it.Now depending
	# upon the profit,
	# either Max_lene we will take
	# it or discard it.
	if (length[n - 1] <= Max_len):
		t[n][Max_len] = max(price[n - 1] + un_kp(price, length, Max_len - length[n - 1], n),
				un_kp(price, length, Max_len, n - 1));
	

	# If the length of the rod is
	# greater than the permitted size,
	# Max_len we will not consider it.
	else:
		t[n][Max_len] = un_kp(price, length, Max_len, n - 1);
	

	# Max_lene Max_lenill return the maximum
	# value obtained, Max_lenhich is present
	# at the nth roMax_len and Max_length column.
	return t[n][Max_len];


if __name__ == '__main__':

	price = [1, 5, 8, 9, 10, 17, 17, 20 ];
	n =len(price);
	length = [0]*n;
	for i in range(n):
		length[i] = i + 1;
	
	Max_len = n;
	print("Maximum obtained value is " ,un_kp(price, length, n, Max_len));



4) Dynamic Programming Approach Iterative Solution

# Python program for above approach


def cutRod(prices, n):
	mat = [[0 for i in range(n+1)]for j in range(n+1)]
	for i in range(1, n+1):
		for j in range(1, n+1):
			if i == 1:
				mat[i][j] = j*prices[i-1]
			else:
				if i > j:
					mat[i][j] = mat[i-1][j]
				else:
					mat[i][j] = max(prices[i-1]+mat[i][j-i], mat[i-1][j])
	return mat[n][n]


prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(prices)

print("Maximum obtained value is ", cutRod(prices, n))







