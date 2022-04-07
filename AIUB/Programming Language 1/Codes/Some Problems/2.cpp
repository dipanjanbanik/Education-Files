#include<stdio.h>
#include<cmath>
int main()
{
	int a, b;

	for(a=1; a<11; a++)
	{
		printf("Square of %d = ", a);
		b = pow(a,2);
		printf("%d\n", b);
	}

}
