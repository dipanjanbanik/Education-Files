#include <iostream>
using namespace std;

class bank
{
	public:
		int accountid,acountbalance,amount;
		int choice,amount1,amount2,amount3,amount4;
		bank ();
		bank (int,int);
		void calculation ();
		void showinformation();
		void deposite(int amount);
		void withdraw(int amount);
		void transfermoney(int acc, int amount);
};

bank::bank()
{
	cout << "Welcome to our bank\n\n";
	cout << "Enter account number:";
	cin >> accountid;
	cout << "\n" << "Enter your deposite amount:";
	cin >> amount;
	deposite (amount);	
}


void bank::showinformation()
{
	if (choice==3)
	{
		cout << "\n";
		cout << "Your deposite ammount is:" << amount << "\n";
		cout << "Your total balance is:" << amount;
	}
	
	else if (choice==1)
	{
		cout << "\n";
		cout << "Your deposite ammount is:" << amount << "\n"; 
		cout << "Your withdraw amount is:" << amount2 << "\n";
		cout << "Your total balance is:" << amount1;
	}
	
	else if (choice==2)
	{
		cout << "\n";
		cout << "Your deposite ammount is:" << amount << "\n"; 
		cout << "Your transfered amount is:" << amount3 << "\n";
		cout << "Your total balance is:" << amount4;
	}
}


void bank::deposite(int amount)
{
	cout << "\n" << "You want to withdraw or transfer money?\n" << "(for withdraw press 1 & for transfer press 2 & for leave press 3):";
	cin >> choice;
	cout << "\n";
	if (choice==1)
	withdraw(amount);
	else if (choice==2)
	transfermoney(accountid, amount);
	else if (choice==3)
	showinformation();
}


void bank::withdraw(int amount)
{
	cout << "How much money you want to withdraw:";
	cin >> amount2;
	amount1=amount-amount2;
	showinformation ();
}


void bank::transfermoney(int acc, int amount)
{
	int a;
	cout << "Which account you want to transfer:";
	cin >> a;
	cout << "\n" << "How much money you want to transfer:";
	cin >> amount3;
	amount4=amount-amount3;
	showinformation();
}


int main ()
{
	bank ob;
}
