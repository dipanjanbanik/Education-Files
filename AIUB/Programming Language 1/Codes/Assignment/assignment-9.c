/*A positive integer is entered through the keyboard. Write a program to obtain
the prime factors of this number. For example, prime factors of 24 are 2, 2, 2
and 3, whereas prime factors of 35 are 5 and 7.*/


#include<stdio.h>

int main()
{
	int i,j, num;
	i=2;

	printf("Enter an integer: ");
	scanf("%d", &num);

	while(i<=num)
		{
			if(num%i==0)
				{
					num=num/i;
					printf("%d", i);
					
					if(num/i==0)
					printf("");
					else
					printf(",");
					
					i=1;
				}
			i++;
		}
}
