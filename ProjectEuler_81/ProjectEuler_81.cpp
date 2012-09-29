#include <iostream>
#include <fstream>

using namespace std;

/* Can be solved similar to triangle percolation
Each stage is the top-left upside-down L slice from array
cumsum along row, and along column
percolate smallest sum to next stage, all the way to finish, always compare left and top value
*/

int main(int argc, char const *argv[])
{
	int data[80][80]; // Matrix of values to be loaded
	ifstream indata;
	int n; // holds value
	char m; // holds comma
	
	// Load data from file
	indata.open("matrix.txt");
	if (!indata) {
		cerr << "Error opening file." << endl;
		return -1;
	}
	for (int col = 0; col < 80; ++col) {
		for (int row = 0; row < 79; ++row)
		{
			indata >> n >> m;
			data[col][row] = n;
		}
		// Last row doesn't have comma after
		indata >> n;
		data[col][79] = n;
	}
	indata.close();

	// cumsum along starting row col (top and left edge of matrix)
	for (int i = 1; i < 80; ++i)
	{
		data[0][i] += data[0][i-1]; // row
		data[i][0] += data[i-1][0]; // col
	}

	// For each slice in, add min of cell to left or above, continue till at bottom-right
	for (int k = 1; k < 80; ++k)
	{
		// Take care of corner value
		data[k][k] += min(data[k][k-1],data[k-1][k]); // row
		// Do rest of slice
		for (int i = k+1; i < 80; ++i)
		{
			// cell += min( left cell, top cell )
			data[k][i] += min(data[k][i-1],data[k-1][i]); // row
			data[i][k] += min(data[i-1][k],data[i][k-1]); // row
		}
	}

	cout << "Sum of best path: " << data[79][79] << endl;
	
	return 0;
}