#include<iostream>
using namespace std;

int main()
	{
	int i,j,k,row;

	for(i=10; i>=1; i--)
		{
		for(j=10; j>i; j--)
			{
			cout << " ";
			}
		for(k=1; k<(i*2); k++)
			{
			cout << "*";
			}
		cout << "\n";
		}
	}
