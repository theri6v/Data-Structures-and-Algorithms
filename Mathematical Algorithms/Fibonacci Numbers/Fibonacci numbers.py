1. Pattern in Last digits of Fibonacci numbers : 
Last digits of first few Fibonacci Numbers are : 

0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, ... 

'''Python3 program to demonstrate that sequence of last digits of Fibonacci numbers repeats after 60'''


if __name__=='__main__':
	max = 100
	arr = [0 for i in range(max)]
	arr[0] = 0
	arr[1] = 1

# storing Fibonacci numbers
	for i in range(2, max):
		arr[i] = arr[i - 1] + arr[i - 2]

	# Traversing through store numbers
	for i in range(1, max - 1):
		

	# Since first two number are 0 and 1
	# so, if any two consecutive number encounter 0 and 1
	# at their unit place, then it clearly means that
	# number is repeating/ since we just have to find
	# the sum of previous two number
		if((arr[i] % 10 == 0) and (arr[i + 1] % 10 == 1)):
			break

	print("Sequence is repeating after index", i)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


2. Factors of Fibonacci number : On careful observation, we can observe the following thing :

Every 3-rd Fibonacci number is a multiple of 2
Every 4-th Fibonacci number is a multiple of 3
Every 5-th Fibonacci number is a multiple of 5
Every 6-th Fibonacci number is a multiple of 8

'''Python3 program to demonstrate divisibility of Fibonacci numbers'''
MAX = 90; 

# indexes variable stores index of number 
# that is divisible by 2, 3, 5 and 8 
arr = [0] * (MAX);
index1 = [0] * (MAX);
index2 = [0] * (MAX); 
index3 = [0] * (MAX);
index4 = [0] * (MAX); 

# storing fibonacci numbers 
arr[0] = 0; 
arr[1] = 1; 
for i in range(2, MAX): 
	arr[i] = arr[i - 1] + arr[i - 2]; 

# c1 keeps track of number of index 
# of number divisible by 2 and others 
# c2, c3 and c4 for 3, 5 and 8 
c1, c2, c3, c4 = 0, 0, 0, 0;

# separating fibonacci number into
# their respective array 
for i in range(MAX): 
	if (arr[i] % 2 == 0): 
		index1[c1] = i;
		c1 += 1;
	if (arr[i] % 3 == 0): 
		index2[c2] = i;
		c2 += 1;
	if (arr[i] % 5 == 0): 
		index3[c3] = i;
		c3 += 1;
	if (arr[i] % 8 == 0): 
		index4[c4] = i;
		c4 += 1;

# printing index arrays 
print("Index of Fibonacci numbers",
		"divisible by 2 are :"); 
for i in range(c1): 
	print(index1[i], end = " "); 
print(""); 

print("Index of Fibonacci number", 
		"divisible by 3 are :"); 
for i in range(c2): 
	print(index2[i], end = " "); 
print(""); 

print("Index of Fibonacci number", 
		"divisible by 5 are :"); 
for i in range(c3): 
	print(index3[i], end = " "); 
print(""); 

print("Index of Fibonacci number", 
		"divisible by 8 are :"); 
for i in range(c4): 
	print(index4[i], end = " "); 
print("");

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Fibonacci number with index number factor : We have some Fibonacci number like F(1) = 1 which is divisible by 1, F(5) = 5 which is divisible by 5, F(12) = 144 which is divisible by 12, F(24) = 46368 which is divisible by 24, F(25) = 75025 which is divisible by 25. This type of index number follow a certain pattern. First, let’s keep a look on those index number : 
1, 5, 12, 24, 25, 36, 48, 60, 72, 84, 96, 108, 120, 125, 132, ….. 

On observing it, this series is made up of every number that is multiple of 12 as well as all the number that satisfies the condition of pow(5, k), where k = 0, 1, 2, 3, 4, 5, 6, 7, …….

 '''Python3 program to demonstrate that Fibonacci numbers that are divisible by their indexes have indexes as either power of 5 or multiple of 12'''

if __name__=='__main__':
	MAX = 100
# storing Fibonacci numbers
	arr = [0 for i in range(MAX)]
	arr[0] = 0
	arr[1] = 1
	for i in range(2, MAX):
		arr[i] = arr[i - 1] + arr[i - 2]

	print("Fibonacci numbers divisible by their indexes are :")
	for i in range(1, MAX):
		if(arr[i] % i == 0):
			print(i,end=" ")





