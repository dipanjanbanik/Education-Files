#include<iostream>
#include<string>
using namespace std;


class student
{
	private:
	bool regconfirm;
	
	public:
	string studentid, name;
	double cgpa;
	int credittaken;
	student();
	student(string, string, double, int);
	friend int isregistered(student ob);
	void showinfo();
};


//constructors
student::student()
{
	cout<<"empty constructor \n\n" <<endl;
}


student::student(string id, string nm, double gpa, int ctaken)
{
	studentid=id;
	name=nm;
	cgpa=gpa;
	credittaken=ctaken;

	cout<<"constructor with parameter \n\n" <<endl;
}


int isregistered(student ob)
{
	if(ob.studentid=="14-xxxxx-2")
		return true;
	 if(ob.studentid!="14-xxxxx-2")
		return false;
}


int main()
{
	student o;
	student o1("14-xxxxx-2", "Sabiha Tasnim Tisha", 3.01, 12);
	
	if(isregistered(o1)==true)
		cout<<"registered";
	else if(isregistered(o1)==false)
		cout<<"not registered";
}
