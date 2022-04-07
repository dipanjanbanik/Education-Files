#include<stdio.h>

int main()
{
	int a, b;
	
	printf("Size of long is %d ", sizeof(a));
	printf("Enter an Integer: ");
	scanf("%d", &a);
	if(a%2==0)
	printf("Even number");
	else
	printf("Odd number");
}
