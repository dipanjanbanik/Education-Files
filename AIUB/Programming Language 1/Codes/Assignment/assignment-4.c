/*Write a program which finds out average marks of some students*/


#include<stdio.h>

int main()
{
	int student, course, i, j;
	int rollno[50], marks[10], average[50];

	printf("How many students do you have: ");
	scanf("%d", &student);

	printf("How many courses each student have: ");
	scanf("%d", &course);


	for(i=1; i<=student; i++)
		{
			marks[0]=0;
			printf("\nEnter student #%d roll no: ", i);
			scanf("%d", &rollno[i]);
			printf("Enter student #%d marks \n", i);
			printf("-----------------------------\n");
			
			for(j=1; j<=course; j++)
				{
					printf("Course %d:", j);
					scanf("%d", &marks[j]);
					marks[0]=marks[0]+marks[j];
				}
				average[i]=marks[0]/course;
		}
		
		printf("\n\n\n");
		
		for(i=1; i<=student; i++)
		{
			printf("=== student#%d ===\n", i);
			printf("Roll no: %d\n", rollno[i]);
			printf("Average marks: %d\n\n", average[i]);
		}

}
