//Write a program to Convert 

//i) Decimal to Binary 


#include <stdio.h>
 
int main()
{
    int num, reminder, base, binary, decimal;
    binary=0;
    base=1;
 
    printf("Enter a decimal input: ");
    scanf("%d", &num);
    
    while (num>0)
    {
        reminder = num%2;
        binary = binary+reminder*base;
        base = base*10;
        num = num/2;
    }
    
    printf("Binary output is: %d\n\n\n", binary);
    

    
//ii) Binary to Decimal number

    decimal=0;
    base=1;
 
    printf("Enter a binary input: ");
    scanf("%d", &num);
        
    while (num>0)
    {
        reminder = num%10;
        decimal = decimal+reminder*base;
        num = num/10 ;
        base = base*2;
    }
   
    printf("Decimal output is: %d", decimal);

}
