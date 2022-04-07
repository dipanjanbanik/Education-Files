#include <stdio.h>
int main()
{
    int a,b,c,d,e,f,g,h,x,sum;
    printf ("Enter your 5 digit number:");
    scanf ("%d",&x);
    a=x/10000;
    printf ("Your first digit is:%d\n",a);
    b=x%10000;
    c=b/1000;
    printf ("Your second digit is:%d\n",c);
    d=x%1000;
    e=d/100;
    printf ("Your third digit is:%d\n",e);
    f=x%100;
    g=f/10;
    printf ("Your fourth digit is:%d\n",g);
    h=x%10;
    printf ("Your fifth digit is:%d\n",h);
    sum=a+c+e+g+h;
    printf ("Your reverse 5 digit number is:%d%d%d%d%d\n",h,g,e,c,a);
}
