#include <stdio.h>
int main ()
{
	int x,y,z;
	printf ("Enter your cost price:");
	scanf ("%d",&x);
	printf ("Enter your selling price:");
	scanf ("%d",&y);
	if (x>y)
	{
		z=x-y;
		printf ("You have made loss and your loss is:%d",z);
	}
	else if (x<y)
	{
		z=y-x;
		printf ("You have made profit and your profit is:%d",z);
	}
	else if (x=y)
	{
		printf ("You neither made loss & neither made profit");
	}
	getch();
}
