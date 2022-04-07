#include <stdio.h>

int main()
{
	int a;
	printf("Enter number: ");
	scanf("%d", &a);
	if(a>0)
		printf("%d is a positive number", a);
	else if(a<0)
		printf("%d is a negetive number", a);
	else
		printf("%d is zero", a);
}
