#include<iostream>
using namespace std;

int main()
	{
		int i, j, k;
		
	for(int i=0; i<=10; i++)
		{
		for(int k=1; k<=10-i; k++)
			{
			printf("  ");
			}
		for(int j=0; j<i; j++)
			{
			cout << " *";
			}
		cout << "\n";
		}
	}
