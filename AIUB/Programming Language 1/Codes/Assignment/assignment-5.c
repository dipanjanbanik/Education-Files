/*A B C D E F G
A B C D E F
A B C D E 
A B C D 
A B C 
A B
A*/


#include<stdio.h>

int main()
{
	int row, column, k;
	k=65;
	
    for( row=7; row>=0; row--)
    {
            for( column=row; column>0; column--)
            {
                    printf(" %c ", k);
                    k++;
            }
            k=65;
            printf("\n");
    }
    
}
