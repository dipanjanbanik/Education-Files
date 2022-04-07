#include <stdio.h>
#include <conio.h>
int main ()
{
    float a,b,c,d;
    printf ("Enter your first triangle angle:");
    scanf ("%f",&a);
    printf ("Enter your second triangle angle:");
    scanf ("%f",&b);
    printf ("Enter your third triangle angle:");
    scanf ("%f",&c);
    d=a+b+c;
    if (d==180)
    printf ("Your triangle total sum is %f & it is valid",d);
    else
    printf ("Your triangle total sum is %f & it is not valid",d);
    printf ("\n\n");
    getch ();
    printf ("Press any key to exit");
}
