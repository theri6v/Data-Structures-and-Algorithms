What are Prime Numbers?
A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself. 

In other words, the prime number is a positive integer greater than 1 that has exactly two factors, 1 and the number itself. First few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 . . .

Note: 1 is not either prime or composite. The remaining numbers, except for 1, are classified as prime and composite numbers.

Properties of Prime Numbers:
Every number greater than 1 can be divided by at least one prime number.
Every even positive integer greater than 2 can be expressed as the sum of two primes.
Except 2, all other prime numbers are odd. In other words, we can say that 2 is the only even prime number.
Two prime numbers are always coprime to each other.
Each composite number can be factored into prime factors and individually all of these are unique in nature.
Prime Numbers and Co-prime numbers:
It is important to distinguish between prime numbers and co-prime numbers. Listed below are the differences between prime and co-prime numbers.

Coprime numbers are always considered as a pair, whereas a prime number is a single number.
Co-prime numbers are numbers that have no common factor except 1. In contrast, prime numbers do not have such a condition.
A co-prime number can be either prime or composite, but its greatest common factor (GCF) must always be 1. Unlike composite numbers, prime numbers have only two factors, 1 and the number itself.
Example of co-prime: 13 and 15 are co-primes. The factors of 13 are 1 and 13 and the factors of 15 are 1, 3 and 5. We can see that they have only 1 as their common factor, therefore, they are coprime numbers.
Example of prime: A few examples of prime numbers are 2, 3, 5, 7 and 11 etc.
How to check whether a number is Prime or not? 

  
'''Naive Approach: The naive approach is to'''

  # Python3 program to check whether a number
# is prime or not using recursion

# Function check whether a number
# is prime or not


def isPrime(n, i):

	# Corner cases
	if (n == 0 or n == 1):
		return False

	# Checking Prime
	if (n == i):
		return True

	# Base cases
	if (n % i == 0):
		return False

	i += 1

	return isPrime(n, i)


# Driver Code
if (isPrime(35, 2)):
	print("true")
else:
	print("false")


'''Efficient Approach: An efficient solution is to:'''

Iterate through all numbers from 2 to ssquare root of n and for every number check 
if it divides n [because if a number is expressed as n = xy and any of the x or y is greater than the root of n, 
the other must be less than the root value]. If we find any number that divides, we return false.

Below is the implementation:

 # A school method based Python3 program
# to check if a number is prime
 
 
# import sqrt from math module
from math import sqrt
 
 
 
# Function check whether a number
# is prime or not
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True
 
 
# Driver Code
if __name__ == '__main__':
    if isPrime(11):
        print("true")
    else:
        print("false")



'''Another Efficient approach: To check whether  the number is prime or not follow the below idea'''

We will deal with a few numbers such as 1, 2, 3, and the numbers which are divisible by 2 and 3 in separate cases and for remaining numbers.
Iterate from 5 to sqrt(n) and check for each iteration whether (that value) or (that value + 2) divides n or not and increment the value by 6 
[because any prime can be expressed as 6n+1 or 6n-1]. If we find any number that divides, we return false.

Below is the implementation for the above idea:

 import math
 
def is_prime(n: int) -> bool:
     
    # Check if n=1 or n=0
    if n <= 1:
        return "false"
     
    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return "true"
     
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return "false"
     
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return "false"
 
    return "true"
 
if __name__ == '__main__':
    print(is_prime(11))
