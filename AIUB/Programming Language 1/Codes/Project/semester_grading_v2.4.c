/*Semester grading report using 4-D array, function, structure*/

#include<stdio.h>
#include<string.h>
#include<windows.h>

struct student
{
	char lettergrade[15][8][2];
	float result[15][2][8][9];
	float calculation[15][8][8];
	float cgpa[15];
	int credit[15][2];
	int subject[15][2];
	float currentcgpa;
};

struct student obj[15], sub[15], calc[15], cg, currcgpa;

int counter=0, semester;




float print(int sub, int s)
{
	int i, j, k, l, m;
	m=1;

	for(i=0; i<sub; i++)
	{
		printf("Course %d\t", m++);
		for(j=counter; j<counter+1; j++)
		{
			l=0;
			while(l<6)
			{
				if(l==2)
				{
					printf("\t  %.2f\t", obj[s].result[s][j][i][l]);
					l++;
				}
				else if(l==3)
				{
					printf("\t %.2f\t    ", obj[s].result[s][j][i][l]);
					l++;
				}
				else if(l==4)
				{
					printf("\t%.2f\t", obj[s].result[s][j][i][l]);
					l++;
				}
				else if(l==5)
				{
					printf("      %.2f\t\t", obj[s].result[s][j][i][l]);
					l++;
				}
				else
				{
					printf("%.2f\t  ", obj[s].result[s][j][i][l]);
					l++;
				}
			}
			printf("%.2f", obj[s].result[s][j][i][6]);
		}
		printf("\n\n");
	}

	counter++;
	s++;
}




float show(int sub, int s)
{
	int i, j, k, l, m, n;
	m=1;
	printf("\t\t\t\t\t\t\tMidterm Result\n");
	printf("\t\t-----------------------------------------------------------------------------------------------\n");
	printf("\t\tQuiz 1\t  Quiz 2\tAttandance\tPerformance\tWritten\t   Quiz total\t   Final Result\n");
	print(sub, s);
	printf("\n\n\t\t\t\t\t\t\tFinalterm Result\n");
	printf("\t\t-----------------------------------------------------------------------------------------------\n");
	printf("\t\tQuiz 1\t  Quiz 2\tAttandance\tPerformance\tWritten\t   Quiz total\t   Final Result\n");
	print(sub, s);
	printf("\n\n\t\t\t\t\t     Final Result\n");
	printf("\t\t---------------------------------------------------------------------\n");
	printf("\t\tMidterm (40)\tFinalterm (60)\tTotal (100)\tLettergrade\tcgpa\n");
	counter=0;

	for(i=0; i<sub; i++)
	{
		printf("Course %d\t", m++);

		printf("%.2f\t\t", calc[s].calculation[s][i][0]);
		printf("%.2f\t\t", calc[s].calculation[s][i][1]);
		printf("%.2f\t\t", calc[s].calculation[s][i][2]);
		for(j=0; j<2; j++)
		{
			printf("%c", calc[s].lettergrade[s][i][j]);
		}
		if(i==sub-1)
			printf("");
		else
			printf("\n");
	}
	printf("\t\t%.2f\n\n\n\n", cg.cgpa[s]);
}




float checkgrade(float check, int count, int sem)
{
	int i, j;
	if(check>=94.00)
	{
		calc[sem].calculation[sem][count][3]=4.00;
		strcpy(calc[sem].lettergrade[sem][count], "A+");
	}

	else if(check>=90.00 && check<=93.00)
	{
		calc[sem].calculation[sem][count][3]=3.75;
		strcpy(calc[sem].lettergrade[sem][count], "A");
	}

	else if(check>=86.00 && check<=89.99)
	{
		calc[sem].calculation[sem][count][3]=3.50;
		strcpy(calc[sem].lettergrade[sem][count], "A-");
	}

	else if(check>=82.00 && check<=85.99)
	{
		calc[sem].calculation[sem][count][3]=3.25;
		strcpy(calc[sem].lettergrade[sem][count], "B+");
	}

	else if(check>=78.00 && check<=81.99)
	{
		calc[sem].calculation[sem][count][3]=3.00;
		strcpy(calc[sem].lettergrade[sem][count], "B");
	}

	else if(check>=74.00 && check<=77.99)
	{
		calc[sem].calculation[sem][count][3]=2.75;
		strcpy(calc[sem].lettergrade[sem][count], "B-");
	}

	else if(check>=70.00 && check<=73.99)
	{
		calc[sem].calculation[sem][count][3]=2.50;
		strcpy(calc[sem].lettergrade[sem][count], "C+");
	}

	else if(check>=66.00 && check<=69.99)
	{
		calc[sem].calculation[sem][count][3]=2.25;
		strcpy(calc[sem].lettergrade[sem][count], "C");
	}

	else if(check>=62.00 && check<=65.99)
	{
		calc[sem].calculation[sem][count][3]=2.00;
		strcpy(calc[sem].lettergrade[sem][count], "C-");
	}

	else if(check>=58.00 && check<=61.99)
	{
		calc[sem].calculation[sem][count][3]=1.75;
		strcpy(calc[sem].lettergrade[sem][count], "D+");
	}

	else if(check>=54.00 && check<=57.99)
	{
		calc[sem].calculation[sem][count][3]=1.50;
		strcpy(calc[sem].lettergrade[sem][count], "D");
	}

	else if(check>=50.00 && check<=53.99)
	{
		calc[sem].calculation[sem][count][3]=1.00;
		strcpy(calc[sem].lettergrade[sem][count], "D-");
	}

	else if(check>=0.00 && check<=49.99)
	{
		calc[sem].calculation[sem][count][3]=0.00;
		strcpy(calc[sem].lettergrade[sem][count], "F");
	}

}




float calculation(int sub, float credit, int semi)
{
	int i, j, k;
	float temp=0.00;

	for(i=0; i<2; i++)
	{
		for(j=0; j<sub; j++)
		{
			obj[semi].result[semi][i][j][5]=obj[semi].result[semi][i][j][0]+obj[semi].result[semi][i][j][1];
			obj[semi].result[semi][i][j][6]=obj[semi].result[semi][i][j][2]+obj[semi].result[semi][i][j][3]+obj[semi].result[semi][i][j][4]+obj[semi].result[semi][i][j][5];

			//printf("semester %d term %d sub %d total= %f\n",semi, i, j, obj[semi].result[semi][i][j][6]);			debug result
		}
	}

	for(j=0; j<sub; j++)
	{
		calc[semi].calculation[semi][j][0]=obj[semi].result[semi][0][j][6]*0.4;
		//printf("semester %d term 0 sub %d total(40)= %f\n",semi, j, calc[semi].calculation[semi][j][0]);			debug result

		calc[semi].calculation[semi][j][1]=obj[semi].result[semi][1][j][6]*0.6;
		//printf("semester %d term 1 sub %d total(60)= %f\n",semi, j, calc[semi].calculation[semi][j][1]);			debug result

		calc[semi].calculation[semi][j][2]=calc[semi].calculation[semi][j][0]+calc[semi].calculation[semi][j][1];
		//printf("semester %d term_total sub %d total(100)= %f\n",semi, j, calc[semi].calculation[semi][j][2]);		debug result

		checkgrade(calc[semi].calculation[semi][j][2], j, semi);
		calc[semi].calculation[semi][j][4]=calc[semi].calculation[semi][j][3]*3.00;
	}

	for(i=0; i<sub; i++)
	{
		temp=temp+calc[semi].calculation[semi][i][4];
	}

	cg.cgpa[semi]=temp/credit;
	//printf("semester %d cgpa= %f\n",semi, cg.cgpa[semi]);															debug result
}




void current()
{
	int i, j;
	float temp, temp1;
	temp=temp1=0;

	for(i=0; i<semester; i++)
	{
		for(j=0; j<currcgpa.subject[i][0]; j++)
		{
			temp1=temp1+calc[i].calculation[i][j][4];
		}
		temp=temp+currcgpa.credit[i][0];
	}
	currcgpa.currentcgpa=temp1/temp;
	printf("\n\n\n\t\t\t\t\t**************");
	printf("///Current CGPA is %.2f\\\\\\", currcgpa.currentcgpa);
	printf("**************\n\n\n\n");
}




int main()
{
	SMALL_RECT rect;										//change the window size of console application
	COORD coord;											//source from
	coord.X = 150; 											//http://stackoverflow.com/questions/30973260/dev-c-console-window-properties
	coord.Y = 350;

	rect.Top = 0;
	rect.Left = 0;
	rect.Bottom = coord.Y-1;
	rect.Right = coord.X-1;

	HANDLE hwnd = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleScreenBufferSize(hwnd, coord);
	SetConsoleWindowInfo(hwnd, TRUE, &rect);

	int subject, quizcount, temp, i, j, k, o, s;
	o=1;
	float totalcredit;

	printf("Enter total number of semester: ");
	scanf("%d", &semester);

	if(semester>15 || semester<=0)
	{
		while(semester>15 || semester<=0)
		{
			printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[Currenty this project support up to 15 semester]\n");
			printf("Enter total number of semester: ");
			scanf("%d", &semester);
		}
	}

	for(s=0; s<semester; s++)
	{
		printf("\n\t\t\t +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n");
		printf("\t\t\t +				     Semester %d			  	     +\n", o++);
		printf("\t\t\t +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n");

		printf("How many subject you have taken for this semester: ");
		scanf("%d", &subject);

		if(subject>8 || subject<=0)
		{
			while(subject>8 || subject<=0)
			{
				printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[You can only take up to 8 subject]\n");
				printf("How many subject you have taken for this semester: ");
				scanf("%d", &subject);
			}
		}
		
		currcgpa.subject[s][0]=subject;
		totalcredit=subject*3.00;
		currcgpa.credit[s][0]=totalcredit;
		printf("\n\n");

		for(i=0; i<2; i++)
		{
			if(i==0)
			{
				printf("\t\t\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
				printf("\t\t\t\t\t\t   |Enter your mid term results|\n\n");
				printf("\t\t\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n");
			}
			else
			{
				printf("\t\t\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
				printf("\t\t\t\t\t\t  |Enter your final term results|\n\n");
				printf("\t\t\t\t\t\t   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n");
			}

			temp=1;

			for(j=0; j<subject; j++)
			{
				printf("\t\t\t-------------------------------\n");
				printf("\t\t\t|    Enter course %d Results    |\n", temp);
				printf("\t\t\t-------------------------------\n");
				temp++;

				k=0;
				while(k<5)
				{
					quizcount=1;
					while(quizcount<3)
					{
						printf("Enter quiz %d marks: ", quizcount);
						scanf("%f", &obj[s].result[s][i][j][k]);
						if(obj[s].result[s][i][j][k]<=20.00 && obj[s].result[s][i][j][k]>=0)
						{
							quizcount++;
							k++;
						}
						else
							printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[Quiz count as highest 20 marks]\n");
					}
					while(k<3)
					{
						printf("Enter Attendance marks: ");
						scanf("%f", &obj[s].result[s][i][j][k]);
						if(obj[s].result[s][i][j][k]<=10.00 && obj[s].result[s][i][j][k]>=0)
							k++;
						else
						{
							printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[Attendance count as highest 10 marks]\n");
						}
					}
					while(k<4)
					{
						printf("Enter performance marks: ");
						scanf("%f", &obj[s].result[s][i][j][k]);
						if(obj[s].result[s][i][j][k]<=10.00 && obj[s].result[s][i][j][k]>=0)
							k++;
						else
						{
							printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[Performance count as highest 10 marks]\n");
						}
					}
					while(k<5)
					{
						printf("Enter written exam marks: ");
						scanf("%f", &obj[s].result[s][i][j][k]);
						if(obj[s].result[s][i][j][k]<=40 && obj[s].result[s][i][j][k]>=0)
							k++;
						else
						{
							printf("\t\t\t\t\t\t\t!!!Wrong input!!!\t[Written Exam count as highest 40 marks]\n");
						}
					}
				}
			}
		}
		calculation(subject, totalcredit, s);
		printf("\n\n\n");
		show(subject, s);
	}
	current();
	
	getch();
}


/*
created     - 13-DEC-2015 04:50 AM
modified    - 31-DEC-2015 12:35 PM
*/
