#include <stdio.h>
int main ()
{
	int a,b,c,d,e,x,y;
	printf ("Enter first subject:");
	scanf ("%d",&a);
	printf ("Enter second subject:");
	scanf ("%d",&b);
	printf ("Enter third subject:");
	scanf ("%d",&c);
	printf ("Enter fourth subject:");
	scanf ("%d",&d);
	printf ("Enter fifth subject:");
	scanf ("%d",&e);
	x=a+b+c+d+e;
	printf ("Total marks:%d\n",x);
	y=x/5;
	printf ("Total percentage:%d\n",y);
}
