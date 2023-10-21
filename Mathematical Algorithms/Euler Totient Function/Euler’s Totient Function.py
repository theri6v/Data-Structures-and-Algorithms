Euler’s Totient function Φ (n) for an input n is the count of numbers in {1, 2, 3, …, n-1} that are relatively prime to n, i.e., the numbers whose GCD (Greatest Common Divisor) with n is 1.

Examples :

Φ(1) = 1  
gcd(1, 1) is 1

Φ(2) = 1
gcd(1, 2) is 1, but gcd(2, 2) is 2.

Φ(3) = 2
gcd(1, 3) is 1 and gcd(2, 3) is 1

Φ(4) = 2
gcd(1, 4) is 1 and gcd(3, 4) is 1

Φ(5) = 4
gcd(1, 5) is 1, gcd(2, 5) is 1, 
gcd(3, 5) is 1 and gcd(4, 5) is 1

Φ(6) = 2
gcd(1, 6) is 1 and gcd(5, 6) is 1, 
How to compute Φ(n) for an input nΦ
A simple solution is to iterate through all numbers from 1 to n-1 and count numbers with gcd with n as 1. Below is the implementation of the simple method to compute Euler’s Totient function for an input integer n. 

----------------------------------------------------------------------------------------------------------------------------------------------
'''A simple Python3 program to calculate Euler's Totient Function'''
 
# Function to return
# gcd of a and b
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# A simple method to evaluate
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
 
# Driver Code
for n in range(1, 11):
    print("phi(",n,") = ", 
           phi(n), sep = "")

----------------------------------------------------------------------------------------------------------------------------------------------

The formula basically says that the value of Φ(n) is equal to n multiplied by-product of (1 – 1/p) for all prime factors p of n. For example value of Φ(6) = 6 * (1-1/2) * (1 – 1/3) = 2.
We can find all prime factors using the idea used in this post. 

1) Initialize : result = n
2) Run a loop from 'p' = 2 to sqrt(n), do following for every 'p'.
     a) If p divides n, then 
           Set: result = result  * (1.0 - (1.0 / (float) p));
           Divide all occurrences of p in n.
3) Return result  
Below is the implementation of Euler’s product formula.  

 '''Python 3 program to calculate Euler's Totient Function using Euler's product formula'''
 
def phi(n) :
 
    result = n   # Initialize result as n
      
    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while p * p<= n :
 
        # Check if p is a prime factor.
        if n % p == 0 :
 
            # If yes, then update n and result
            while n % p == 0 :
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p = p + 1
         
         
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if n > 1 :
        result -= result // n
  #Since in the set {1,2,....,n-1}, all numbers are relatively prime with n
  #if n is a prime number
  
    return int(result)
     
     
# Driver program to test above function
for n in range(1, 11) :
    print("phi(", n, ") = ", phi(n))

----------------------------------------------------------------------------------------------------------------------------------------------

We can avoid floating-point calculations in the above method. The idea is to count all prime factors and their multiples 
and subtract this count from n to get the totient function value (Prime factors and multiples of prime factors won’t have gcd as 1) 


1) Initialize result as n
2) Consider every number 'p' (where 'p' varies from 2 to Φn). 
If p divides n, then do the following
   a) Subtract all multiples of p from 1 to n [all multiples of p
      will have gcd more than 1 (at least p) with n]
   b) Update n by repeatedly dividing it by p.
   
3) If the reduced n is more than 1, then remove all multiples
   of n from the result.
   
Below is the implementation of the above algorithm. 

 '''Python3 program to calculate Euler's Totient Function def phi(n)'''
     
    # Initialize result as n
    result = n; 
 
    # Consider all prime factors
    # of n and subtract their
    # multiples from result
    p = 2; 
    while(p * p <= n):
         
        # Check if p is a 
        # prime factor.
        if (n % p == 0): 
             
            # If yes, then 
            # update n and result
            while (n % p == 0):
                n = int(n / p);
            result -= int(result / p);
        p += 1;
 
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most 
    # one such prime factor)
    if (n > 1):
        result -= int(result / n);
    return result;
 
# Driver Code
for n in range(1, 11):
    print("phi(",n,") =", phi(n));
