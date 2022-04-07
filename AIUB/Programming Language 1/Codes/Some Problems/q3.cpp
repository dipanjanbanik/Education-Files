//Q3

#include<stdio.h>

int main()
{
	int num,r,c,sp,x;
	printf("Enter loop repeat number(rows):");
	scanf("%d",&num);
	for(r=1; num>=r; r++)
		{
			for(sp=num-r; sp>=1; sp--)
				printf(" ");
			for(c=1; c<=r; c++)
				printf("%d",c);
			for(x=r-1; x>=1; x--)
				printf("%d",x);
			printf("\n");
		}
}
