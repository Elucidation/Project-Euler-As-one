#include <iostream>
using namespace std;

// Can be solved mathematically
// largest product of range of small primes < n = 1e6
// = 2 * 3 * 5 * 7 * 11 * 13 * 17 = 510510


// Semi-brute force solution below
pair<int*,int> primesieve(int n) {
	// Returns pair (pointer to array of primes, number of primes)
	// Primes in array are all primes less than or equal to n
	int primeCount = 0;
	int* arr = new int[n];
	for (int i = 0; i < n; ++i)
		arr[i] = i+1;
	arr[0] = 0;
	for (int i = 0; i < n; ++i)
	{
		// arr[0] = 0, arr[1] = 2, arr[2] = 3
		if (arr[i]==0)
			continue;
		primeCount++;
		// cout << "Prime " << arr[i] << " count(" << primeCount << ")" << endl;
		for (int j = i+i+1; j < n; j+=i+1)
		{
			// Sieve out all arr[j] from arr
			arr[j] = 0;
		}
	}
	int* primes = new int[primeCount];
	for (int i = 0, j = 0; i < n; ++i)
	{
		if (arr[i] != 0) {
			primes[j++] = arr[i];
		}
	}
	delete[] arr;

	return pair<int*,int>(primes,primeCount);
}

int main(int argc, char const *argv[])
{
	int n = int(1e6) + 1; 

	// Get Primes into table
	pair<int*,int> primepair = primesieve(n+1);
	int* primes = primepair.first;
	int primeCount = primepair.second;

	// Solve problem
	int bestN;
	float bestRatio=0;
	for (int i = 2; i < n; ++i) {
		float d = i;
		for (int j = 0; j < primeCount && primes[j] <= i; ++j)
			if (i % primes[j] == 0)
				d *= 1. - 1./primes[j];

		if (d > 0 && i/d > bestRatio) {
			bestRatio = i/d;
			bestN = i;
			cout << "New Best: n/phi(n) = " << i << "/" << d << " = " << i/d << endl;;
		}
	}
	cout << "Solution: Best ratio " << bestRatio << ", with n = " << bestN << endl;
	// Best of n = 510510 w/ ratio 510510/92160 = 5.53939

	delete[] primes;
	return 0;
}