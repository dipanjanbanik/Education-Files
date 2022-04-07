#include <stdio.h>
int main()
{
	float a,b,x,sum;
	printf ("Enter your basic salary:");
	scanf ("%f",&x);
	a=x*0.4;
	printf ("Your dearness allowance is:%f\n",a);
	b=x*0.2;
	printf ("Your house rent allowance is:%f\n",b);
	a+b;
	printf ("Your total dearness allowance & house rent is:%f\n",a+b);
	sum=x-(a+b);
	printf ("Your gross salary is:%f\n",sum);
}
