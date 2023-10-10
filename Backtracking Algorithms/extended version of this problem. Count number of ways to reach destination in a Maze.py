class Solution:
	def solve(self, i, j, arr, n, ans, move, direction, dir1, djr, visited):
	#if we reach the last cell of the matrix. just add the current move to the list of answers (ans) and return from the function, effectively stopping any further exploration.
		if i == n - 1 and j == n - 1:
			ans.append(move)
			return
		
		for ind in range(4):
		#calculate the next row index based on the current i (row) and the di array, which holds values for direction changes.
			nexti = i + dir1[ind]
			#calculate the next column index based on the current j (column) and the dj array, which holds values for direction changes.
			nextj = j + djr[ind]
			# to check whether is is valid to move to the next cell
	# make sure to check if the next cell has been visited before.
			
			if 0 <= nexti < n and 0 <= nextj < n and visited[nexti][nextj] == 0 and arr[nexti][nextj] == 1:
			#Also Mark the current cell as visited to prevent revisiting it during the same path exploration. 
			visited[i][j] = 1
			#Recursively call the solve function with the updated position , the updated path move(adding the current direction), and the current direction), and the updated state information.
			self.solve(nexti, nextj, arr, n, ans, move + direction[ind], direction, dir1, djr, visited)
			# Reset the current cell's visited status to 0 to allow backtracking(an essential step)
			visited[i][j] = 0

	def findPath(self, m, n):
	#we intialise with array to get all the required values.
		ans = []
		#initialise a string direction which represents all the directions.
		direction = "DLRU"
		dir1 = [1, 0, 0, -1]
		djr = [0, -1, 1, 0]
		#for visited cell
		visited = [[0 for _ in range(n)] for _ in range(n)]
		
		#if top-left corner of the grid is equal to 1 to verify if there is a valid starting point in the grid.
		if m[0][0] == 1:
			self.solve(0, 0, m, n, ans, "", direction, dir1, djr, visited)

		return ans

if __name__ == "__main__":
	n = 4
	m = [
		[1, 0, 0, 0],
		[1, 1, 0, 1],
		[1, 1, 0, 0],
		[0, 1, 1, 1]
	]

	obj = Solution()
	result = obj.findPath(m, n)
	if len(result) == 0:
		print(-1)
	else:
		for path in result:
			print(path, end=" ")
		print()
