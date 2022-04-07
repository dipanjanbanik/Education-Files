#include <stdio.h>

int main()
{
	char a;
	printf("Enter a character: ");
	scanf("%c", &a);
	if(a>'A' && a<'Z')
		printf("%c is a character", a);
	else if(a>'a' && a<'z')
		printf("%c is a character", a);
	else
		printf("%c is not a character", a);
}
