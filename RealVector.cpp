#include "RealVector.hpp"
#include <cmath>

RealVector::RealVector() {}
RealVector::RealVector(float x, float y) {
    this->x = x;
    this->y = y;
}

RealVector RealVector::add(RealVector vec) {
    return RealVector(x+vec.x, y+vec.y);
}
RealVector RealVector::sub(RealVector vec) {
    return RealVector(x-vec.x, y-vec.y);
}
RealVector RealVector::mult(float num) {
    return RealVector(x*num, y*num);
}
float RealVector::get_mag() {
    return sqrt(x*x + y*y);
}
float RealVector::angle_of() {
    if (x == 0) return y>=0 ? M_PI/2 : (3*M_PI)/2;
    float angle = atan(y/x);
    
    if (y < 0 && x < 0) angle += M_PI; //We're in the 3rd quadrant, our angle was outputted in the 1st
    else if (x < 0) angle += M_PI; //We're in the 2nd quadrant, our angle was outputted in the 4th
    return angle; 
}