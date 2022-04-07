#include<iostream>
#include<string>
using namespace std;


class account
{
	private:
		string name, acid, nominee;
		int balance, age, wdraw, dpsit;
		
	public:
		account();
		account(string, string, string, int, int);
		
		void deposite(int);
		void withdraw(int);
		
		void setName(string);
		void setID(string);
		void setBalance(int);
		void setAge(int);
		void setNominee(string);
		
		string getName();
		string getID();
		int getBalance();
		int getAge();
		string getNominee();
		int getDeposite();
		int getWithdraw();
};


//constructors
account::account()
{
	cout<<"constructor with empty parameter \n\n" << endl;
}

account::account(string nm, string id, string nomin, int amount, int ag)
{
	name=nm;
	acid=id;
	nominee=nomin;
	balance=amount;
	age=ag;
	
	cout<<"constructor with parameter \n\n" << endl;
}


//setter methods
void account::setName(string nm)
{
	name=nm;
}

void account::setID(string roll)
{
	acid=roll;
}

void account::setBalance(int amount)
{
	balance=amount;
}

void account::setAge(int ag)
{
	age=ag;
}

void account::setNominee(string nomin)
{
	nominee=nomin;
}


//getter methods
string account::getName()
{
	return name;
}

string account::getID()
{
	return acid;
}

int account::getBalance()
{
	return balance;
}

string account::getNominee()
{
	return nominee;
}

int account::getAge()
{
	return age;
}

int account::getDeposite()
{
	return dpsit;
}

int account::getWithdraw()
{
	return wdraw;
}


//deposite & withdraw
void account::deposite(int amount)
{
	dpsit=amount;
	balance = balance+amount;
}

void account::withdraw(int amount)
{
	wdraw=amount;
	balance = balance-amount;
}


//main
int main()
{
	account o;
	account o1("", "", "", 0, 0);
	o1.setName("Sabiha Tasnim Tisha");
	o1.setID("14-xxxxx-1");
	o1.setAge(20);
	o1.setNominee("Banik");
	o1.setBalance(50000);
	
	cout<< "Name is: "	  << 	o1.getName() << endl;
	cout<< "ID is: 	 "	  << 	o1.getID() << endl;
	cout<< "Age is:  " 	  << 	o1.getAge() << endl;
	cout<< "Nominee is: " <<    o1.getNominee() << endl;
	cout<< "Balance is: " << 	o1.getBalance() << endl;
	
	o1.deposite(5000);
	o1.withdraw(10000);
	
	cout<< "Deposite amount: " << o1.getDeposite() <<endl;
	cout<< "Withdraw amount: " << o1.getWithdraw() <<endl;
	cout<< "Current balance: " << o1.getBalance() <<endl;
}


