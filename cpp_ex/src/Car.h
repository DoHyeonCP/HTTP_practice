#ifndef CAR_H
#define CAR_H

#pragma once

#include<string>
using namespace std;

class Car
{
    int speed;
    int gear;
    string color;

public:
    int getSpeed();
    void setSpeed(int s);


};

#endif