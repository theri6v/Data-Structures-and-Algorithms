'''Python code for the above approach'''

n = 6

# Loop through each row of
# the pattern
for row in range(1, n+1):

	# Loop through each column of
	# the pattern
	for col in range(1, row+1):

		# If the column number is even,
		# print a "#" character
		if col % 2 == 0:
			print("#", end="")

		# If the column number is odd,
		# print a "*" character
		else:
			print("*", end="")

	# Move to the next line after
	# printing each row
	print()
