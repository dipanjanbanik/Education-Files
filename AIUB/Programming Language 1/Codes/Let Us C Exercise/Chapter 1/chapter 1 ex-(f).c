#include<stdio.h>
void main()
{
    int a,b;
    printf("Enter value of a :");
    scanf("%d",&a);
    printf("Enter value of b :");
    scanf("%d",&b);
      
    a=a+b;
    b=a-b;
    a=a-b;
      
    printf("\nAfter swaping the value of a=%d and b=%d ",a,b);
          
}
