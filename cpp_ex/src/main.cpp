#include <iostream>
#include <string>
#include "Car.h"

using namespace std;
int main(int argc, char *argv[])
{
    Car myCar;

    myCar.setSpeed(100);

    cout << "�ӵ� : " << myCar.getSpeed() << endl;

    return 0;
}
