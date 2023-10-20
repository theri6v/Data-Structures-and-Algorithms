Method 1 :

We know, LCM(a, b)=\frac{a*b}{gcd(a, b)}                                        
The above relation only holds for two numbers, 
LCM(a, b, c)\neq \frac{a*b*c}{gcd(a, b, c)}                

The main steps of our algorithm are: 

Initialize ans = arr[0].
Iterate over all the elements of the array i.e. from i = 1 to i = n-1 
At the ith iteration ans = LCM(arr[0], arr[1], …….., arr[i-1]). This can be done easily as LCM(arr[0], arr[1], …., arr[i]) = LCM(ans, arr[i]). Thus at i’th iteration we just have to do ans = LCM(ans, arr[i]) = ans x arr[i] / gcd(ans, arr[i]) 
 
Below is the implementation of the above algorithm : 

 # Python Program to find LCM of n elements
 
def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm
     
l = [2, 7, 3, 9, 4]
 
num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)
 
for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])
     
print(lcm)
 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below is the implementation of the above algorithm Recursively :

 def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)
 
# recursive implementation
def LcmOfArray(arr, idx):
   
    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = LcmOfArray(arr, idx+1)
    return int(a*b/__gcd(a,b)) # __gcd(a,b) is inbuilt library function
 
arr = [1,2,8,3]
print(LcmOfArray(arr, 0))
arr = [2,7,3,9,4]
print(LcmOfArray(arr,0))

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Method 3: This code uses the reduce function from the functools library and the gcd function from the math library to find the LCM of a list of numbers. 
The reduce function applies the lambda function to the elements of the list, cumulatively reducing the list to a single value (the LCM in this case). 
The lambda function calculates the LCM of two numbers using the same approach as the previous implementation. The final LCM is returned as the result.

 from functools import reduce
import math
 
def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)
 
numbers = [2, 3, 4, 5]
print("LCM of", numbers, "is", lcm(numbers))

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Method 4: Using Euclidean algorithm 

The function starts by initializing the lcm variable to the first element in the array. It then iterates through the rest of the array, and for each element, it calculates the GCD of the current lcm and the element using the Euclidean algorithm. The calculated GCD is stored in the gcd variable.

Once the GCD is calculated, the LCM is updated by multiplying the current lcm with the element and dividing by the GCD. This is done using the formula LCM(a,b) = (a * b) / GCD(a,b).

 def lcm_of_array(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        num1 = lcm
        num2 = arr[i]
        gcd = 1
        # Finding GCD using Euclidean algorithm
        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp
        gcd = num1
        lcm = (lcm * arr[i]) // gcd
    return lcm
 
 
# Example usage
arr1 = [1, 2, 8, 3]
arr2 = [2, 7, 3, 9, 4]
print(lcm_of_array(arr1))  # Output: 24
print(lcm_of_array(arr2))  # Output: 252

