#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;

int main() 
{
	enum Fruits{orange=5, guava=9, apple=7};
    Fruits myFruit=orange;
     int i;
     cout << "Please enter the fruit of your choice(0 to 2)::";
     cin >> i;
     switch(i) 
       {
         case orange:
         cout << "Your fruit is orange";
         break;
         case guava:
         cout << "Your fruit is guava";
         break;
         case apple:
         cout << "Your fruit is apple";
         break;
      }
      
      if (myFruit == orange)
      cout<<myFruit;
     return 0;
}
