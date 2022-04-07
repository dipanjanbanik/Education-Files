/*
    1
  121
 12321
1234321
*/



#include<stdio.h>

int main()
{

    int row, column, x, y;
 
    for(row=1; row<=4; row++)
    {
        for(x = 4-row; x>=1; x--)
        printf(" ");
        for(column=1; column<=row; column++)
         printf("%d", column);
        for(y = row-1; y>=1; y--)
         printf("%d", y);
        
        printf("\n");
    }

} 