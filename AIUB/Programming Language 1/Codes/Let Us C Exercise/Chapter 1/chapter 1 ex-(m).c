#include <stdio.h>
int main()
{
    int a,b,c,d,e,f,g,h,i,j,k,l,m,x;
    printf ("Enter your 5 digit number:");
    scanf ("%d",&x);
    a=x/10000;
    i=a+1;
    printf ("By adding your first digit is:%d\n",i);
    b=x%10000;
    c=b/1000;
    j=c+1;
    printf ("By adding your second digit is:%d\n",j);
    d=x%1000;
    e=d/100;
    k=e+1;
    printf ("By adding your third digit is:%d\n",k);
    f=x%100;
    g=f/10;
    l=g+1;
    printf ("By adding your fourth digit is:%d\n",l);
    h=x%10;
    m=h+1;
    printf ("By adding your fifth digit is:%d\n",m);
    printf ("By adding your 5 digit number is:%d%d%d%d%d\n",i,j,k,l,m);
}
