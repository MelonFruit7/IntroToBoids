#pragma once
#include "RealVector.hpp"

class Boid {
    public:
        RealVector position, velocity;
        float danger_zone, sight_zone, size;

        Boid();
        Boid(float x, float y, float vx, float vy, float danger_zone, float sight_zone, float size);

        void move_boid();
        void show_boid();
};