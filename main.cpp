#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    const double PI = 3.14159265358979;
    int choice;
    double width, height, radius, base;
    double area;

    cout << "Geometry Calculator\n";
    cout << "\t1. Calculate the Area of Circle\n";
    cout << "\t2. Calculate the Area of Rectangle\n";
    cout << "\t3. Calculate the Area of Triangle\n";
    cout << "\t4. Quit\n\n";
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    switch(choice) {
        case 1:
            cout << "Enter the radius: ";
            cin >> radius;
            area = PI * pow(radius, 2);
        case 2:
            cout << "Enter the width: ";
            cin >> width;
            cout << "Enter the height: ";
            cin >> height;
            area = width * height;
        case 3:
            cout << "Enter the base: ";
            cin >> base;
            cout << "Enter the height: ";
            cin >> height;
            area = 0.5 * base * height;
        case 4:
            cout << "Program Stopped"
            exit(0);
            }

    cout << left << setprecision(2) << fixed;
    cout << "The area is " << area << endl;

    return 0;
}
