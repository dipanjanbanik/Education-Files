#include<iostream>
using namespace std;

int main()
	{
	int pin = 1234, pass = 789, tamount = 100000, epin, epass, wamount ;
	char yn;

	cout << "Enter your pin number: ";
	cin >> epin;
	cout << "Enter your password: ";
	cin >> epass;

	do
		{

		if (epin==pin && epass==pass)
			{
			cout << "Your total balance is: "<< tamount << endl;
			cout << "Do you want to withdraw your money (press y / n): ";
			cin >> yn;

			if(yn=='y')
				{
				cout << "How much money you want to withdraw: ";
				cin >> wamount;

				if(wamount>tamount)
					{
					cout << "You dont have suffecient balance to withdraw" << endl;
					}
				else
					{
					tamount = tamount - wamount;
					}
				}
			}
			
		else if (epin!=pin || epass!=pass)
			{
			cout << "Your entered pin or password is incorrect. Do you want try again? (press y / n): ";
			cin >> yn;

			if (yn=='y')
				{
				cout << "Enter your pin number: ";
				cin >> epin;
				cout << "Enter your password: ";
				cin >> epass;
				}
			}

		}
	while (yn!='n');

	}
