#include <stdio.h>
int main ()
{
	int x,y,a,b,c,d,e,f,g,h,i,j;
	printf ("Enter your 5 digit number:");
	scanf ("%d",&x);
	a=x%10;//---------------------
	b=x/10;
	c=b%10;//---------------------
	d=b/10;
	e=d%10;//---------------------
	f=d/10;
	g=f%10,//---------------------
	h=f/10;//---------------------
	printf ("Your reverse digit is:%d%d%d%d%d\n",a,c,e,g,h);
	i=h+g+e+c+a;
	j=a+c+e+g+h;
	if (x==(a&&c&&e&&g&&h))
	printf ("Your reverse digits are equal\n");
	else if (i!=j)
	printf ("Your reverse digit are not equal\n");
}
