/*Write a program to Find out prime numbers between 1 to 100*/


#include<stdio.h>

int main()
{
    int i, j, n;
    n=0;
    
    printf("Prime number between 1-100 is:\n");
    
    for(i=2;i<=100;i++)
    {
        for(j=1;j<=i;j++)
        {
            if(i%j==0)
            {
              n++;
            }
        }
        if(n==2)
        printf("%d\n",i);
        n=0;
    }
    
}