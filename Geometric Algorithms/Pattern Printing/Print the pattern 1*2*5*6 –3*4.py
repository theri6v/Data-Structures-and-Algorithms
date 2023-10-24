'''Python code to print the above pattern'''

# Function to print the pattern

def printPattern(n):
	l = []
	num = 1

	# First Traversal top to bottom
	for i in range(n):
		tem = []
		for j in range((i)*2):
			tem.append(' ')
		for j in range(n - i):
			tem.append(num)
			tem.append('*')
			num += 1
		l.append(tem)

	# Second Traversal bottom to top
	for i in range(n-1, -1, -1):
		tem = []
		for j in range(0, n-i):
			tem.append(num)
			tem.append('*')
			num += 1
		tem.pop()
		l[i] += tem

	for row in l:
		for i in row:
			print(i, end ="")
		print()


# Driver code
if __name__ == '__main__':
	N = 3

	# Function call
	printPattern(N)
