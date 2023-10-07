'''Python3 program for activity selection problem when input activities may not be sorted'''

from heapq import heappop, heappush

# Function to select activites


def SelectActivities(s, f):
	ans = []
	p = []

	# Pushing elements in the list
	for i, j in zip(s, f):
		heappush(p, (j, i))

	it = heappop(p)
	start = it[1]
	end = it[0]
	ans.append(it)

	# Sorting process
	while p:
		it = heappop(p)
		if it[1] >= end:
			start = it[1]
			end = it[0]
			ans.append(it)

	print("Following Activities should be selected.\n")
	for f, s in ans:
		print(f"Activity started at {s} and ends at {f}")


# Driver code
if __name__ == "__main__":
	s = [1, 3, 0, 5, 8, 5]
	finish = [2, 4, 6, 7, 9, 9]

	# Function call
	SelectActivities(s, finish)

# This code is contributed by kraanzu.
