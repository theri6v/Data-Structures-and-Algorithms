'''Iterative Approach to Find and Print Nth Fibonacci Numbers'''

#Function for nth fibonacci number - Space Optimisation Taking 1st two fibonacci numbers as 0 and 1



def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
		return b

# Driver Program


print(fibonacci(9))

'''Recursion Approach to Find and Print Nth Fibonacci Numbers'''

# Fibonacci series using recursion
def fibonacci(n):
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
	n = 9
	print(n, "th Fibonacci Number: ")
	print(fibonacci(n))


'''Dynamic Programming Approach to Find and Print Nth Fibonacci Numbers'''

# Fibonacci Series using Dynamic Programming
def fibonacci(n):

	# Taking 1st two fibonacci numbers as 0 and 1
	f = [0, 1]

	for i in range(2, n+1):
		f.append(f[i-1] + f[i-2])
	return f[n]


print(fibonacci(9))

'''Nth Power of Matrix Approach to Find and Print Nth Fibonacci Numbers'''

# Fibonacci Series using
# Optimized Method

# function that returns nth
# Fibonacci number


def fib(n):

	F = [[1, 1],
		[1, 0]]
	if (n == 0):
		return 0
	power(F, n - 1)

	return F[0][0]


def multiply(F, M):

	x = (F[0][0] * M[0][0] +
		F[0][1] * M[1][0])
	y = (F[0][0] * M[0][1] +
		F[0][1] * M[1][1])
	z = (F[1][0] * M[0][0] +
		F[1][1] * M[1][0])
	w = (F[1][0] * M[0][1] +
		F[1][1] * M[1][1])

	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

# Optimized version of
# power() in method 4


def power(F, n):

	if(n == 0 or n == 1):
		return
	M = [[1, 1],
		[1, 0]]

	power(F, n // 2)
	multiply(F, F)

	if (n % 2 != 0):
		multiply(F, M)


# Driver Code
if __name__ == "__main__":
	n = 9
	print(fib(n))








