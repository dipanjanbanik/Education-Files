/*Write a program to print the numbers from 1 to 10 and their squares*/


#include<stdio.h>
#include<math.h>

int main()
{
	int num, sum;
	
	for(num=1; num<=10; num++)
	{
		sum=pow(num,2);
		printf("Square of %d = %d\n", num, sum);
	}
}
