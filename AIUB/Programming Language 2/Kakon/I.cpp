#include<iostream>
using namespace std;

int main()
	{
	int i,j,k,row;

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

	}
