# include <stdio.h>
int main ()
{
int n;
char a[10][10] = {"zero", "one", "two", "three", "four",
"five", "six", "seven", "eight", "nine"};
printf ("Enter the number:\n");
scanf ("%d", &n);
printf ("The given num in word = %s\n", a[n]);
}  
