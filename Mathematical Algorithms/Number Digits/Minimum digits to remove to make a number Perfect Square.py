# Python program to find required minimum 
# digits need to remove to make a 
# number perfect square

import math
# function to check minimum number of
# digits should be removed to make
# this number a perfect square
def perfectSquare(s) :
	
	# size of the string
	n = len(s)

	# our final answer
	ans = -1

	# to store string which is
	# perfect square.
	num = ""

	# We make all possible subsequences
	for i in range(1, (1 << n)) :
		str = ""
		
		for j in range(0, n) :
			
			# to check jth bit is
			# set or not.
			if ((i >> j) & 1) :
				str = str + s[j]

		# we do not consider a number 
		# with leading zeros
		if (str[0] != '0') :
			
			# convert our temporary 
			# string into integer
			temp = 0;
			for j in range(0, len(str)) :
				temp = (temp * 10 +
				(ord(str[j]) - ord('0')))

			k = int(math.sqrt(temp))

			# checking temp is perfect 
			# square or not.
			if (k * k == temp) :
				
				# taking maximum sized
				# string
				if (ans < len(str)) :
					ans = len(str)
					num = str

	if (ans == -1) :
		return ans
	else :		 
		
		# print PerfectSquare
		print ("{} ".format(num), end="")
		return n - ans
	
# Driver code
print (perfectSquare("8314"))
print (perfectSquare("753"));

