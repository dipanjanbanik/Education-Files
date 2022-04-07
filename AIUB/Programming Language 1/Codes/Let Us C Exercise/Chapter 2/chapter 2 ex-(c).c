#include <stdio.h>
int main ()
{
	int x,y;
	printf ("Enter your desire year:");
	scanf ("%d",&x);
	y=x%4;
	if (y==0)
	printf ("Your inputed year is a leap year");
	else if (y!=0)
	printf ("Your inputed year is not a leap year");
	getch();
}
