'''Python3 program to compute Binomial Probability''' 

# function to calculate nCr i.e., 
# number of ways to choose r out 
# of n objects 
def nCr(n, r): 
	
	# Since nCr is same as nC(n-r) 
	# To decrease number of iterations 
	if (r > n / 2): 
		r = n - r; 

	answer = 1; 
	for i in range(1, r + 1): 
		answer *= (n - r + i); 
		answer /= i; 

	return answer; 

# function to calculate binomial r.v. 
# probability 
def binomialProbability(n, k, p): 

	return (nCr(n, k) * pow(p, k) *
						pow(1 - p, n - k)); 

# Driver code 
n = 10; 
k = 5; 
p = 1.0 / 3; 

probability = binomialProbability(n, k, p); 

print("Probability of", k, 
	"heads when a coin is tossed", end = " "); 
print(n, "times where probability of each head is", 
									round(p, 6)); 
print("is = ", round(probability, 6)); 

