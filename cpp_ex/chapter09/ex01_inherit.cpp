#include <iostream>
#include <string>
using namespace std;
class Shape {
    int x, y;
public:
    Shape() {
    cout << "Shape() constructor" << endl;
    } 
    Shape(int xloc, int yloc): x(xloc), y(yloc) {
    cout << "Shape(xloc, yloc) constructor" << endl;
    } 
    ~Shape() {
    cout << "~Shape() destructor" << endl;
    }
};

class Rectangle: public Shape {
    int width, height;
public:
    Rectangle() {
    cout << "Rectangle() constructor" << endl;
    } 
    Rectangle(int x,int y, int w, int h): Shape(x, y), width(w), height(h) {
    cout << "Rectangle(x, y, w, h) constructor" << endl;
    } 
    ~Rectangle() {
    cout << "~Rectangle() destructor" << endl;
    }
};

int main(int argc, char const *argv[])
{
    Rectangle r1;
    cout << endl;
    Rectangle r2(0, 0, 100, 100);
    cout << endl;
    return 0;
}
