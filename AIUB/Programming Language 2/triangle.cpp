#include<iostream>
#include<string>
using namespace std;


class triangle
{
	private:
		int x, y, z;
		string info;

	public:
		triangle();
		triangle(int, int, int);
		void showInfo();
		void testTriangle();
};


//constructors
triangle::triangle()
{
	cout<<"constructor without parameter \n\n" << endl;
}

triangle::triangle(int a, int b, int c)
{
	x=a;
	y=b;
	z=c;
	cout<<"constructor with parameter \n\n" << endl;
	
	cout<<"Values are: " << a <<", "<< b <<", "<< c <<endl;
}


//test
void triangle::testTriangle()
{
	if (x==y && x==z && y==z)
		info="EQUILATERAL";

	else if(x==y || x==z || y==z)
		info="ISOSCELES";

	else
		info="SCALENE";
}


//show
void triangle::showInfo()
{
	cout<< "Result of the triangle is: " << info;
}


int main()
{
	triangle o;
	triangle o1(4, 4, 5);
	o1.testTriangle();
	o1.showInfo();
}
