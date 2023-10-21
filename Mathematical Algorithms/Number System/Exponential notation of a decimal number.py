Given a positive decimal number, find the simple exponential notation (x = a·10^b) of the given number. Examples:

Input : 100.0
Output : 1E2
Explanation:
The exponential notation of 100.0 is 1E2.

Input :19
Output :1.9E1
Explanation:
The exponential notation of 16 is 1.6E1.
Approach: The simplest way is to find the position of the first non zero digit and the position of the dot. 
The difference between that positions is the value of b (if the value is positive you should also decrease it by one). 
Below is the implementation of the above approach: 

'''Python3 code to find the exponential notation'''

# function to calculate the exponential
# notation
def FindExponent(s, n):
	# Storing the result in an array
	res = []
	i = 0
	while (s[i] in '.0'):
		i += 1
	
	j = n - 1
	while (s[j] in '.0' ):
		j -= 1
		
	# Finding the first index in s which is equal to '.'
	if '.' in s:
		c = s.index('.')
	# if '.' not found then put c = n.
	else:
		c = n

	res.append(s[i]);
	
	if (i != j):
		res.append('.');
		
	for k in range(i + 1, 1 + j):
		if (s[k] != '.'):
			res.append(s[k]);

	if (i < c):
		b = c - i - 1;
	
	else:
		b = c - i;
	
	
	if (b != 0):
		res.append("E");
		res.append(str(b));
	
	print("".join(res))

# main function
s = "100";
n = len(s)
FindExponent(list(s), n);

