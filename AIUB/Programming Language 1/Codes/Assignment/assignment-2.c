/*To join Bangladesh Airforce in the Education Branch the candidate can be male or female in
gender, candidate’s marital status should be single, age should be in between 18 to 21 and
height should be equal or more than 5.2 for female and 5.5 for male. Check the eligibility of a
candidate.*/


#include<stdio.h>

int main()
{
	int age;
	char gender, marital;
	float height;

	printf("Enter candidate's gender (press 'M' for male & press 'F' for female): ");
	scanf("%c", &gender);

	printf("Enter candidate's marital status (press 'S' for single & press 'M' for married): ");
	scanf(" %c", &marital);

	printf("Enter candidate's age: ");
	scanf("%d", &age);

	printf("Enter candidate's height: ");
	scanf("%f", &height);

	printf("\n");

	if(gender=='m' || gender=='M')
		{
			if(marital=='s' || marital=='S' )
				{
					if(age>=18 && age<=21)
						{
							if(height>=5.5)
								printf("Candidate meet's the requirement");
							else
								printf("Candidate doesn't meet the requirement");;
						}
					else
						printf("Candidate doesn't meet the requirement");;
				}
			else
				printf("Candidate doesn't meet the requirement");;
		}

	else if(gender=='f' || gender=='F')
		{
			if(marital=='s' || marital=='S')
				{
					if(age>=18 && age<=21)
						{
							if(height>=5.2)
								printf("you are eligible");
							else
								printf("Candidate doesn't meet the requirement");
						}
					else
						printf("Candidate doesn't meet the requirement");
				}
			else
				printf("Candidate doesn't meet the requirement");
		}

	else
		printf("Candidate doesn't meet the requirement");
}
