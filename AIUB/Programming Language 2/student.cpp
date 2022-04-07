#include<iostream>
#include<string>
using namespace std;

class student
{
	private:
		string name, id, department;
		float cgpa;
		
	public:
		student();
		student(string, string, string, float);
		
		void setName(string);
		void setID(string);
		void setDept(string);
		void setCGPA(float);
		
		string getName();
		string getID();
		string getDept();
		float getCGPA();
};


//constructors
student::student()
{
	cout<<"constructor without parameter \n\n" << endl;
}

student::student(string nm, string roll, string dept, float gpa)
{
	name=nm;
	id=roll;
	department=dept;
	cgpa=gpa;
	
	cout<<"constructor with parameter \n\n" << endl; 
}


//setter methods
void student::setName(string nm)
{
	name=nm;
}

void student::setID(string roll)
{
	id=roll;
}

void student::setDept(string dept)
{
	department=dept;
}

void student::setCGPA(float gpa)
{
	cgpa=gpa;
}


//getter methods
string student::getName()
{
	return name;
}

string student::getID()
{
	return id;
}

string student::getDept()
{
	return department;
}

float student::getCGPA()
{
	return cgpa;
}


int main()
{
	student o;
	student o1("", "", "", 0.0);
	
	o1.setName("Sabiha Tasnim Tisha");
	o1.setID("14-xxxxx-2");
	o1.setDept("COE");
	o1.setCGPA(3.01);
	
	cout<<"Name is: 	  " 	<< o1.getName() << endl;
	cout<<"ID is: 		  " 	<< o1.getID() 	<< endl;
	cout<<"Department is:"		<< o1.getDept() << endl;
	cout<<"CGPA is: 	  " 	<< o1.getCGPA() << endl;
}
