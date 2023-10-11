#include <bits/stdc++.h>
using namespace std;

// Print all subsets if there is atleast one subset of set[]
// with sum equal to given sum
bool flag = 0;
void PrintSubsetSum(int i, int n, int set[], int targetSum,
					vector<int>& subset)
{
	// targetSum is zero then there exist a
	// subset.
	if (targetSum == 0) {

		// Prints valid subset
		flag = 1;
		cout << "[ ";
		for (int i = 0; i < subset.size(); i++) {
			cout << subset[i] << " ";
		}
		cout << "]";
		return;
	}

	if (i == n) {
		// return if we have reached at the end of the array
		return;
	}

	// Not considering current element
	PrintSubsetSum(i + 1, n, set, targetSum, subset);

	// consider current element if it is less than or equal
	// to targetSum
	if (set[i] <= targetSum) {

		// push the current element in subset
		subset.push_back(set[i]);

		// Recursive call for consider current element
		PrintSubsetSum(i + 1, n, set, targetSum - set[i],
					subset);

		// pop-back element after recursive call to restore
		// subsets original configuration
		subset.pop_back();
	}
}

// Driver code
int main()
{
	// Test case 1
	int set[] = { 1, 2, 1 };
	int sum = 3;
	int n = sizeof(set) / sizeof(set[0]);
	vector<int> subset;
	cout << "Output 1:" << endl;
	PrintSubsetSum(0, n, set, sum, subset);
	cout << endl;
	flag = 0;
	// Test case 2
	int set2[] = { 3, 34, 4, 12, 5, 2 };
	int sum2 = 30;
	int n2 = sizeof(set) / sizeof(set[0]);
	vector<int> subset2;
	cout << "Output 2:" << endl;
	PrintSubsetSum(0, n2, set2, sum2, subset2);
	if (!flag) {
		cout << "There is no such subset";
	}

	return 0;
}
// This code is contributed by Hem Kishan
