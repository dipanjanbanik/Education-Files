#include <stdio.h>
int main ()
{
	int x;
	printf ("Enter an integer number:");
	scanf ("%d",&x);
	if ((x%2)==1)
	printf ("Your number is an odd number");
	else if ((x%2)==0)
	printf ("Your number is an even number");
	getch();
}
