import sys

# A suffix array based search function to search a given pattern
# 'pat' in given text 'txt' using suffix array suffArr[]
def search(pat, txt, suffArr, n):

	# Get the length of the pattern
	m = len(pat)
	
	# Initialize left and right indexes
	l = 0
	r = n-1
	
	# Do simple binary search for the pat in txt using the built suffix array
	while l <= r:
	
		# Find the middle index of the current subarray
		mid = l + (r - l)//2
		
		# Get the substring of txt starting from suffArr[mid] and of length m
		res = txt[suffArr[mid]:suffArr[mid]+m]
		
		# If the substring is equal to the pattern
		if res == pat:
		
			# Print the index and return
			print("Pattern found at index", suffArr[mid])
			return
		
		# If the substring is less than the pattern
		if res < pat:
		
			# Move to the right half of the subarray
			l = mid + 1
		else:
		
			# Move to the left half of the subarray
			r = mid - 1
			
	# If the pattern is not found
	print("Pattern not found")
	
def buildSuffixArray(txt, n):

	# Create a list of all suffixes
	suffixes = [txt[i:] for i in range(n)]
	
	# Sort the suffixes
	suffixes.sort()
	
	# Create the suffix array
	suffArr = [txt.index(suffix) for suffix in suffixes]
	return suffArr

# Driver program to test above function
def main():
	txt = "banana" # text
	pat = "nan" # pattern to be searched in text

	# Build suffix array
	n = len(txt)
	suffArr = buildSuffixArray(txt, n)

	# search pat in txt using the built suffix array
	search(pat, txt, suffArr, n)
	return 0

if __name__ == '__main__':
	sys.exit(main())

# This code is contributed by Vikram_Shirsat
