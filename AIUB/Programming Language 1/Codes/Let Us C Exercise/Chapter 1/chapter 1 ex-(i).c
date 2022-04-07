#include <stdio.h>
int main ()
{
	int a,b,c,d;
	printf ("Enter your desire 4 digit number:");
	scanf ("%d",&a);
	b=a/1000;
	printf ("First digit:%d\n",b);
	c=a%10;
	printf ("Second digit:%d\n",c);
	d=b+c;
	printf ("Sum between first & last digit is:%d\n",d);
}
