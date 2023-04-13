#include <iostream>
using namespace std;

class Time{
public:
    int hour;
    int minute;

    // Time() {
    // hour = 0;
    // minute = 0;
    // }

    // // »ı¼ºÀÚ
    // Time(int h, int m){
    //     hour = h;
    //     minute = m;
    // }

    // Time(int h=0, int m=0) {
    // hour = h;
    // minute = m;
    // }
    Time(int h = 0, int m = 0) 
        : hour(h), minute(m) {
    }

    void print(){
        cout << hour << ":" << minute << endl;
    }
};

int main() {
    // Time a;
    Time a;
    Time b(10, 25);
    Time c{10, 25};
    Time d= {10, 25};

    a.print();
    b.print();
    c.print();
    d.print();
    return 0;
}