#include<iostream>
using namespace std;

int main()
	{
	int row,i,j;
	
	for(i=10; i>=1; i--)
		{
		for(j=1; j<=i; j++)
			{
			cout << "* ";
			}
		cout << "\n";
		}
	}
