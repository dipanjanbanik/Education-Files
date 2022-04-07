#include <stdio.h>
int main()
{
    float a,b,c;
    printf ("Enter your steel hardness value:");
    scanf ("%f",&a);
    printf ("Enter your steel carbon value:");
    scanf ("%f",&b);
    printf ("Enter your steel tensile value:");
    scanf ("%f",&c);
    if (a>=50&&b<=0.7&&c>=5600)
    printf ("Your steel grade is 10");
    else if (a>=50&&b<=0.7)
    printf ("Your steel grade is 9");
    else if (b<=0.7&&c==5600)
    printf ("Your steel grade is 8");
    else if (a>=50&&c==5600)
    printf ("Your steel grade is 7");
    else if (a>=50||b<=0.7||c==5600)
    printf ("Your steel grade is 6");
    else
    printf ("Your steel grade is 5");
    printf ("\n\n");
    printf ("Press any key to exit");
    getch();
}