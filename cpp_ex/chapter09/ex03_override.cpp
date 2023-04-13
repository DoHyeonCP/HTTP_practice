#include <iostream>
#include <string>
using namespace std;
class SuperClass {
public:
    void print() {
    cout << "SuperClass :: print()" << endl;
    } 
};

class ChildClass : public SuperClass {
public:
    void print() {
    SuperClass::print();
    cout << "ChildClass :: print()" << endl;
    } 
};

int main(int argc, char const *argv[])
{
    ChildClass c;
    c.print();
    // SuperClass :: print()
    // ChildClss :: print()
    return 0;
}

/*
다중상속
class Sub: public Sup1, public Sup2
{
    ... // 추가된 멤버
    ... // 재정의된 멤버
}
*/