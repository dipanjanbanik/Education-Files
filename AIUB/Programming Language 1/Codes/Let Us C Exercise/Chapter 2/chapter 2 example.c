#include <stdio.h>
int main ()
{
	int x;
	char y,z;
	printf ("Type marital status (m or um):");
	scanf ("%c",&y);
	printf ("Type age:");
	scanf ("%d",&x);
	printf ("Type male or female (m or f):");
	scanf ("%c",&z);
	printf ("\n");
	if (y=='m')
	printf ("Driver is insured\n");
	if (y=='um'&&z=='m'&&x>30)
	printf ("Driver is insured\n");
	if (y=='um'&&z=='f'&&x>25)
	printf ("Driver is insured\n");
	else
	printf ("Driver is not insured\n");
	getch();
}
