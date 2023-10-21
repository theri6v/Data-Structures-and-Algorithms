Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 

Example: 

Input : n =10
Output : 2 3 5 7 

Input : n = 20 
Output: 2 3 5 7 11 13 17 19


The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so (Ref Wiki).

Following is the algorithm to find all the prime numbers less than or equal to a given integer n by the Eratosthene’s method: 
When the algorithm terminates, all the numbers in the list that are not marked are prime.
Explanation with Example: 
Let us take an example when n = 50. So we need to print all prime numbers smaller than or equal to 50. 
We create a list of all numbers from 2 to 50.  
Sieve1
According to the algorithm we will mark all the numbers which are divisible by 2 and are greater than or equal to the square of it. 
sieve2
Now we move to our next unmarked number 3 and mark all the numbers which are multiples of 3 and are greater than or equal to the square of it.  
SieveofEratosthenes3
We move to our next unmarked number 5 and mark all multiples of 5 and are greater than or equal to the square of it.  
Sieve4
We continue this process and our final table will look like below:  
Sieve5
So the prime numbers are the unmarked ones: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
Thanks to Krishan Kumar for providing the above explanation.

Implementation: 

Following is the implementation of the above algorithm. In the following implementation, a boolean array arr[] of size n is used to mark multiples of prime numbers. 

 '''Python program to print all primes smaller than or equal to n using Sieve of Eratosthenes'''
  
  
def SieveOfEratosthenes(n): 
  
    # Create a boolean array 
    # "prime[0..n]" and initialize 
    #  all entries it as true. 
    # A value in prime[i] will 
    # finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
  
        # If prime[p] is not 
        # changed, then it is a prime 
        if (prime[p] == True): 
  
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
  
    # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            print(p) 
  
  
# Driver code 
if __name__ == '__main__': 
    n = 20
    print("Following are the prime numbers smaller"), 
    print("than or equal to", n) 
    SieveOfEratosthenes(n) 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
 # Python program for the above approach 
Primes = [0] * 500001
def SieveOfEratosthenes(n) : 
      
    Primes[0] = 1
    i = 3
    while(i*i <= n) :  
        if (Primes[i // 2] == 0) : 
            for j in range(3 * i, n+1, 2 * i) :  
                Primes[j // 2] = 1
                  
        i += 2
          
# Driver Code 
if __name__ == "__main__": 
  
    n = 100
    SieveOfEratosthenes(n) 
    for i in range(1, n+1) : 
        if (i == 2) : 
            print( i, end = " ") 
        elif (i % 2 == 1 and Primes[i // 2] == 0) : 
            print( i, end = " ") 
      
