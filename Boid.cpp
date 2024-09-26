#include "Boid.hpp"
#include "raylib.h"

Boid::Boid() {}
Boid::Boid(float x, float y, float vx, float vy, float danger_zone, float sight_zone, float size) {
    position.x = x;
    position.y = y;
    velocity.x = vx;
    velocity.y = vy;
    this->danger_zone = danger_zone;
    this->sight_zone = sight_zone;
    this->size = size;
}

void Boid::move_boid() {
    int w = GetScreenWidth(), h = GetScreenHeight();
    position = position.add(velocity);
    position.x = position.x > w ? w : position.x < 0 ? 0 : position.x;
    position.y = position.y > h ? h : position.y < 0 ? 0 : position.y;
}

void Boid::show_boid() {
    float mag = velocity.get_mag();

    RealVector u;
    if (mag == 0) u = RealVector(0, -size); //Points up
    else u = velocity.mult(size/mag); //Make our vector the size of the boid
    
    RealVector move_to_middle(-u.x/2, -u.y/2);

    Vector2 tri[3];
    tri[0] = (Vector2){position.x+u.x+move_to_middle.x, position.y+u.y+move_to_middle.y};
    u = RealVector(u.y, -u.x); //90 degree rotation
    tri[1] = (Vector2){position.x+u.x+move_to_middle.x, position.y+u.y+move_to_middle.y};
    u = RealVector(-u.x, -u.y); //180 degree rotation
    tri[2] = (Vector2){position.x+u.x+move_to_middle.x, position.y+u.y+move_to_middle.y};

    DrawTriangleLines(tri[0], tri[1], tri[2], BLACK);
}