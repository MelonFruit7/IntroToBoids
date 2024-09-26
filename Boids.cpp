#include "raylib.h"
#include "Boid.hpp"
#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <time.h>
#include <vector>
using std::vector;
using std::pair;

void limit_speed(Boid &boid, float min_speed, float max_speed) {
    double speed = boid.velocity.get_mag();
    if (speed != 0) {
        if (speed < min_speed) boid.velocity = boid.velocity.mult(min_speed/speed);
        else if (speed > max_speed) boid.velocity = boid.velocity.mult(max_speed/speed);
    } 
}

void bound_boid(Boid &boid, double turn_factor, float turn_padding, int sw, int sh) {
    if (boid.position.x < turn_padding) boid.velocity.x += turn_factor;
    else if (boid.position.x > sw-turn_padding) boid.velocity.x -= turn_factor;
    if (boid.position.y < turn_padding) boid.velocity.y += turn_factor;
    else if (boid.position.y > sh-turn_padding) boid.velocity.y -= turn_factor;
}

void alter_boid_path(vector<Boid> &boids, int boid_idx, double avoidance_factor, double matching_factor, double centering_factor) {
    int neighbors = 0;
    RealVector vel_avg(0, 0);
    RealVector pos_avg(0, 0);
    RealVector close_d(0, 0);

    for (int i = 0; i < boids.size(); i++) {
        if (boid_idx == i) continue;
        
        RealVector diff = boids[boid_idx].position.sub(boids[i].position);

        float pos = diff.get_mag();
        if (pos < boids[boid_idx].danger_zone) {
            if (pos < 1) boids[boid_idx].move_boid();
            close_d = close_d.add(diff);
        } else if (pos < boids[boid_idx].sight_zone) {
            vel_avg = vel_avg.add(boids[i].velocity);
            pos_avg = pos_avg.add(boids[i].position);
            neighbors++;
        }
    }
    if (neighbors > 0) {
        vel_avg = vel_avg.mult(1.0f/neighbors);
        pos_avg = pos_avg.mult(1.0f/neighbors);
        
        RealVector change_vel = vel_avg.sub(boids[boid_idx].velocity).mult(matching_factor);
        boids[boid_idx].velocity = boids[boid_idx].velocity.add(change_vel);

        RealVector change_pos = pos_avg.sub(boids[boid_idx].position).mult(centering_factor);
        boids[boid_idx].velocity = boids[boid_idx].velocity.add(change_pos);
    }
    
    boids[boid_idx].velocity = boids[boid_idx].velocity.add(close_d.mult(avoidance_factor));
}

int main() {
    int screen_width = 1500, screen_height = 1000;
    InitWindow(screen_width, screen_height, "Boids");
    SetTargetFPS(120);

    double avoidance_factor = 0.05, matching_factor = 0.05, centering_factor = 0.0005, turn_factor = 0.2;
    float turn_padding = 100, min_speed = 1.5, max_speed = 6;

    float danger_zone = 15, sight_zone = 40, size = 5;

    srand(time(NULL));
    vector<Boid> boids;
    for (int i = 0; i < 100; i++) {
        float vx = 1, vy = 1;
        if (rand()%2) vx*=-1;
        if (rand()%2) vy*=-1;

        boids.push_back(Boid(rand()%screen_width, rand()%screen_height, vx, vy, danger_zone, sight_zone, size));
    }

    RealVector player(0, 0);
    float player_radius = 100;

    while (!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(WHITE);

        player.x = GetMouseX();
        player.y = GetMouseY();
        DrawCircle(player.x, player.y, player_radius, RED);

        for (int i = 0; i < boids.size(); i++) {
            alter_boid_path(boids, i, avoidance_factor, matching_factor, centering_factor);

            RealVector diff = boids[i].position.sub(player);
            if (diff.get_mag() < boids[i].sight_zone+player_radius) boids[i].velocity = boids[i].velocity.add(diff);

            limit_speed(boids[i], min_speed, max_speed);
            bound_boid(boids[i], turn_factor, turn_padding, screen_width, screen_height);
        }
        for (int i = 0; i < boids.size(); i++) {
            boids[i].move_boid();
            boids[i].show_boid();
        }

        DrawFPS(0, 0);
        EndDrawing();
    }
    CloseWindow();
    return 0;
} 
