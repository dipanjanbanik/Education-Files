#include <stdio.h>

int main()
{
	int a, b, c;
	printf("Enter 3 integer: ");
	scanf("%d %d %d", &a, &b, &c);
	if(a>b && a>c)
		printf("%d is larger", a);
	else if(b>a && b>c)
		printf("%d is larger",b);
	else
		printf("%d is larger",c);
}
