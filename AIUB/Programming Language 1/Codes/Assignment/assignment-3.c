/*Write a program which finds out factorial value(!) for a given input N. Factorial of N can be
found using the following series:  N! = N*(N-1)*(N-2)*....*3*2*1*/


#include<stdio.h>

int main()
{
	int i, factorial, num;
	
	i=factorial=1;

	printf("Enter a number: ");
	scanf("%d",&num);

	while(i<=num)
		{
			factorial= factorial*i;
			i++;
		}

	printf("Factorial value of %d is: %d", num, factorial);
}

