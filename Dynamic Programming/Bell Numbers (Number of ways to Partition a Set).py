# python program to find number of ways of partitioning it.
n = 5
s = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
	for j in range(n+1):
		if j > i:
			continue
		elif(i==j):
			s[i][j] = 1
		elif(i==0 or j==0):
			s[i][j]=0
		else:
			s[i][j] = j*s[i-1][j] + s[i-1][j-1]
ans = 0
for i in range(0,n+1):
	ans+=s[n][i]
print(ans)


# A Python program to find n'th Bell number

def bellNumber(n):

	bell = [[0 for i in range(n+1)] for j in range(n+1)]
	bell[0][0] = 1
	for i in range(1, n+1):

		# Explicitly fill for j = 0
		bell[i][0] = bell[i-1][i-1]

		# Fill for remaining values of j
		for j in range(1, i+1):
			bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

	return bell[n][0]

# Driver program
for n in range(6):
	print('Bell Number', n, 'is', bellNumber(n))
------------------------------------------------------------------------------------------------------


def bell_numbers(n):
	# Initialize the previous row of the Bell triangle with dp[0] = 1
	dp = [1] + [0] * n

	for i in range(1, n+1):
		# The first element in each row is the same as the last element in the previous row
		prev = dp[0]
		dp[0] = dp[i-1]
		for j in range(1, i+1):
			# The Bell number for n is the sum of the Bell numbers for all previous partitions
			temp = dp[j]
			dp[j] = prev + dp[j-1]
			prev = temp

	return dp[0]


n = 5
print(bell_numbers(n))






