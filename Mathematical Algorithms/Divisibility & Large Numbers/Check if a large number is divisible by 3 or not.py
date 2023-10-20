# Python program to find if a number is 
# divisible by 3 or not 

# Function to find that number 
# divisible by 3 or not 
def check(num) : 
	
	# Compute sum of digits 
	digitSum = 0
	while num > 0 : 
		rem = num % 10
		digitSum = digitSum + rem 
		num = num // 10
		
	# Check if sum of digits is 
	# divisible by 3. 
	return (digitSum % 3 == 0) 
	
# main function 
num = 1332
if(check(num)) : 
	print ("Yes") 
else : 
	print ("No") 
	
--------------------------------------------------------------------

Method 2: Checking given number is divisible by 3 or not by using the modulo division operator “%”. 


# Python code 
# To check whether the given number is divisible by 3 or not 

#input 
n=769452
# the above input can also be given as n=input() -> taking input from user 
# finding given number is divisible by 3 or not 
if int(n)%3==0: 
print("Yes") 
else: 
print("No") 



