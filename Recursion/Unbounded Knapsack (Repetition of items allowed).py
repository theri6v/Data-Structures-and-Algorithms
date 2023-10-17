# Python3 program to find maximum 
# achievable value with a knapsack 
# of weight W and multiple instances allowed. 

# Returns the maximum value 
# with knapsack of W capacity 
# A Naive recursive implementation of unbounded Knapsack problem 
def unboundedKnapsack(W, index, val, wt): 

	#Base case of recursion when only one element is there. 
	if index==0 :return (W//wt[0])*val[0] 
	#If the element with referred by index is doesn't occur even once in the required solution 
	notTake=0+unboundedKnapsack(W,index-1,val,wt) 
	#If the element is occur atleast once in the required solution 
	take=-100000
	if wt[index]<=W: 
		take=val[index]+unboundedKnapsack(W-wt[index],index,val,wt) 
	return max(take,notTake)	 


# Driver program 
W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 

print(unboundedKnapsack(W, n-1, val, wt)) 
