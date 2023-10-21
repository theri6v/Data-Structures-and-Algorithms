Method 1:
For a given set[] S, the power set can be found by generating all binary numbers between 0 and 2n-1, where n is the size of the set. 
For example, for the set S {x, y, z}, generate all binary numbers from 0 to 23-1 and for each generated number, the corresponding set can be found by considering set bits in the number.

Below is the implementation of the above approach.

 # python3 program for power set 
  
import math; 
  
def printPowerSet(set,set_size): 
      
    # set_size of power set of a set 
    # with set_size n is (2**n -1) 
    pow_set_size = (int) (math.pow(2, set_size)); 
    counter = 0; 
    j = 0; 
      
    # Run from counter 000..0 to 111..1 
    for counter in range(0, pow_set_size): 
        for j in range(0, set_size): 
              
            # Check if jth bit in the  
            # counter is set If set then  
            # print jth element from set  
            if((counter & (1 << j)) > 0): 
                print(set[j], end = ""); 
        print(""); 
  
# Driver program to test printPowerSet 
set = ['a', 'b', 'c']; 
printPowerSet(set, 3); 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Method 2: (sorted by cardinality)'''

In auxiliary array of bool set all elements to 0. That represent an empty set. Set first element of auxiliary array to 1 and generate all permutations to produce all subsets with one element. 
Then set the second element to 1 which will produce all subsets with two elements, repeat until all elements are included.

Below is the implementation of the above approach.


# Python3 program for the above approach 

# A function which gives previous 
# permutation of the array 
# and returns true if a permutation 
# exists. 
def prev_permutation(str): 

	# Find index of the last 
	# element of the string 
	n = len(str) - 1

	# Find largest index i such 
	# that str[i - 1] > str[i] 
	i = n 
	while (i > 0 and str[i - 1] <= str[i]): 
		i -= 1

	# If string is sorted in 
	# ascending order we're 
	# at the last permutation 
	if (i <= 0): 
		return False

	# Note - str[i..n] is sorted 
	# in ascending order Find 
	# rightmost element's index 
	# that is less than str[i - 1] 
	j = i - 1
	while (j + 1 <= n and str[j + 1] < str[i - 1]): 
		j += 1

	# Swap character at i-1 with j 
	temper = str[i - 1] 
	str[i - 1] = str[j] 
	str[j] = temper 

	# Reverse the substring [i..n] 
	size = n-i+1
	for idx in range(int(size / 2)): 
		temp = str[idx + i] 
		str[idx + i] = str[n - idx] 
		str[n - idx] = temp 

	return True

# Function to print all the power set 
def printPowerSet(set, n): 

	contain = [0 for _ in range(n)] 

	# Empty subset 
	print() 

	for i in range(n): 
		contain[i] = 1

		# To avoid changing original 'contain' 
		# array creating a copy of it i.e. 
		# "Contain" 
		Contain = contain.copy() 

		# All permutation 
		while True: 
			for j in range(n): 
				if (Contain[j]): 
					print(set[j], end="") 
			print() 
			if not prev_permutation(Contain): 
				break

# Driver code 
set = ['a', 'b', 'c'] 
printPowerSet(set, 3) 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''Method 3: We can use backtrack here, we have two choices first consider that element then don’t consider that element'''

Below is the implementation of the above approach.

 # Python3 program to implement the approach 
  
# Function to build the power sets 
def findPowerSet(s, res, n): 
    if (n == 0): 
        for i in res: 
            print(i, end="") 
        print() 
        return
  
    # append the subset to result 
    res.append(s[n - 1]) 
    findPowerSet(s, res, n - 1) 
    res.pop() 
    findPowerSet(s, res, n - 1) 
  
# Function to print the power set 
def printPowerSet(s, n): 
    ans = [] 
    findPowerSet(s, ans, n) 
  
# Driver code 
set = ['a', 'b', 'c'] 
printPowerSet(set, 3) 




