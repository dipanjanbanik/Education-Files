#include <stdio.h>
int main ()
{
    char a;
    printf ("Enter your desire character:");
    scanf ("%c",&a);
    if (a>=65&&a<=90)
    printf ("Your desire character is a capital letter");
    else if (a>=97&&a<=122)
    printf ("Your desire character is a small letter");
    else if (a>=48&&a<=57)
    printf ("Your desire character is a numeric letter");
    else
    printf ("Your desire character is a special symbols");
    printf ("\n\n");
    printf ("Press any key to exit");
    getch ();
}