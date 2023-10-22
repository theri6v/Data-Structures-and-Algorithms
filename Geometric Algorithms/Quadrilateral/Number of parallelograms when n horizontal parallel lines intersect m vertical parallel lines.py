To form a parallelogram, we need two horizontal parallel lines and two vertical parallel lines. So, 
number of ways to choose two horizontal parallel lines are nC2 and number of ways to choose two vertical parallel lines are mC2. So, 
total number of possible parallelogram will be nC2 x mC2.

Below is C++ implementation of this approach: 

# Python Program to find number of parallelogram when
# n horizontal parallel lines intersect m vertical
# parallel lines.
MAX = 10;

# Find value of Binomial Coefficient
def binomialCoeff(C, n, k):
	
	# Calculate value of Binomial Coefficient
	# in bottom up manner
	for i in range(n + 1):
		for j in range(0, min(i, k) + 1):
		
			# Base Cases
			if (j == 0 or j == i):
				C[i][j] = 1;

			# Calculate value using previously
			# stored values
			else:
				C[i][j] = C[i - 1][j - 1] + C[i - 1][j];

# Return number of parallelogram when n horizontal
# parallel lines intersect m vertical parallel lines.
def countParallelogram(n, m):
	C = [[0 for i in range(MAX)] for j in range(MAX)]

	binomialCoeff(C, max(n, m), 2);

	return C[n][2] * C[m][2];

# Driver code
if __name__ == '__main__':
	n = 5;
	m = 5;
	print(countParallelogram(n, m));

----------------------------------------------------------------------------------------------------------------------------


Approach: Using Basic Maths

The same Question can be Solved By just using the basic maths
as we know nC2 = n*(n-1)/2 and same for mC2 so just using basic maths we can solve the question in O(1)

Below is the implementation of the above approach:


#include <iostream>

class GFG {
public:
	static int findtheParallelogram(int n, int m)
	{
		// as nC2 = (n*(n-1))/2
		int result
			= ((n * (n - 1)) / 2) * ((m * (m - 1)) / 2);

		return result;
	}
};

int main()
{
	int n = 5;
	int m = 5;
	std::cout << GFG::findtheParallelogram(n, m)
			<< std::endl;
	return 0;
}

