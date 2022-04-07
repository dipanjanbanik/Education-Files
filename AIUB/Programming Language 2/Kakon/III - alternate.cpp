#include<iostream>
using namespace std;

int main()
	{
	int i,j,k;

	for(i=1; i<=10; i++)
		{
		for(j=i; j<10; j++)
			{
			cout << " ";
			}
		for(k=1; k<(i*2); k++)
			{
			cout << "*";
			}
		cout << "\n";
		}
		
	for(i=9; i>=1; i--)
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
