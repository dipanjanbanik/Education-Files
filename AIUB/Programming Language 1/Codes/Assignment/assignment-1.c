/*In Employee attendance system if an employee maintains 35 hours per week he is considered to
be a regular employee. If an employee maintains 30 hours per week he is considered to be a
moderately regular employee and if an employee maintains less than 30 hours per week he is
considered to be an irregular employee. Write a program to find the status of an employee.*/


#include<stdio.h>

int main()
{
	int hour, weektotal, i;
	
	weektotal=0;
	
	printf("Enter employee's attendance hour in a week \n\n");
	
	for(i=1; i<=7; i++)
	{
		printf("Day %d: ", i);
		scanf("%d", &hour);
		weektotal = weektotal + hour;
	}
	
	printf("\n Total attendance hour in a week is: %d \n", weektotal);
	
	if(weektotal>=35)
	printf("Regular Employee");
	
	else if(weektotal>=30 && weektotal<35)
	printf("Moderately Regular Employee");
	
	else
	printf("Irregular Employee");
	
}
