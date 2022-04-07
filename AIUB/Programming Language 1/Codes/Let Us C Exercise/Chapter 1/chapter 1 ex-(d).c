#include <stdio.h>
int main()
{
	float x,y;
	printf ("Enter fahrenheit:");
	scanf ("%f",&x);
	y=(5.0/9.0)*(x-32);//do not use 5 or 9 use 5.0 or 9.0
	printf ("In centigrade:%f",y);
}
