def generate_palindrome(s, pal):
	n = len(s)

	# Initialize the palindrome matrix for single characters
	for i in range(n):
		pal[i][i] = True

	# Iterate over different lengths of substrings
	for length in range(2, n + 1):
		# Iterate over the starting positions of substrings of current length
		for i in range(n - length + 1):
			# Calculate the ending position of the substring
			j = i + length - 1

			# Check if the characters at the starting and ending positions are equal
			# and if the substring between them is a palindrome or a single character
			if s[i] == s[j] and (length == 2 or pal[i + 1][j - 1]):
				# Mark the substring from i to j as a palindrome
				pal[i][j] = True


def min_cut(s):
	if not s:
		return 0
	n = len(s)

	# 2D list to store whether substring [i, j] is a palindrome
	pal = [[False] * n for _ in range(n)]

	generate_palindrome(s, pal)

	# List to store minimum cuts required to make substring [i, n-1] palindromic
	min_cut_dp = [float('inf')] * n

	# There is no cut required for a single character as it is always a palindrome
	min_cut_dp[0] = 0

	# Iterate over the given string
	for i in range(1, n):
		# Check if string 0 to i is a palindrome. Then minCut required will be 0.
		if pal[0][i]:
			min_cut_dp[i] = 0
		else:
			for j in range(i, 0, -1):
				# If s[i] and s[j] are equal and the inner substring [i+1, j-1]
				# is a palindrome or it has a length of 1
				if pal[j][i]:
					# Update the minimum cuts required if cutting at position 'j+1' results in a smaller value
					if min_cut_dp[j - 1] + 1 < min_cut_dp[i]:
						min_cut_dp[i] = min_cut_dp[j - 1] + 1

	# Return the minimum cuts required for the entire string 's'
	return min_cut_dp[n - 1]


# Driver code
if __name__ == "__main__":
	str = "ababbbabbababa"

	cuts = min_cut(str)
	print("Minimum cuts required:", cuts)
