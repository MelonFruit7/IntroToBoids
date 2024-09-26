from manim import *

class sc(Scene):
    def center_code_around(self, code, line):
        self.play(code.animate.move_to(ORIGIN + DOWN*code[2][line].get_y()))

    def construct(self):
        rec = Rectangle(width=14, height=0.75, color=BLACK, z_index=1).to_edge(UP*0.01)
        rec.set_fill(BLACK, 1)
        self.add(rec)

        boids_file = Text("Boids.cpp").scale(0.25).center().to_edge(UP)
        self.add(boids_file.set_z_index(2))

        code = Code("assets/code/mainv5.cpp", line_spacing=0.8, font_size=9, line_no_from=26).next_to(rec, DOWN)
        to_load = [[code[2][0:1], code[2][33:34]], # Function
                [code[2][1:5]], # Variables 
                [code[2][6:7], code[2][20:21]], # Boid loop
                [code[2][7:8]], # Continue edge case
                [code[2][9:10]], # Diff between boids
                [code[2][11:13], code[2][15:16], code[2][19:20]], # if in range
                [code[2][13:15]], # close_d update
                [code[2][16:19]], # vel_avg & pos_avg update
                [code[2][21:22], code[2][30:31]], # if boid has neighbors in sight
                [code[2][22:24]], # average the averages
                [code[2][25:27]], # apply alignment
                [code[2][28:30]], # apply cohesion
                [code[2][32:33]]] # apply seperation
        for chunk in to_load:
            for c in chunk:
                c.set_opacity(0)

        self.play(DrawBorderThenFill(code))
        self.wait(2)

        for i, (chunk, w_time) in enumerate(zip(to_load, [5, 5, 3, 2, 4, 6, 8, 8, 2, 5, 12, 1, 8])):
            for c in chunk:
                c.set_opacity(1)
                self.play(Write(c))
            if (i == 11):
                self.wait(12)
                self.play(FadeOut(code))
                arrow_vel = Arrow(start=ORIGIN, end=ORIGIN+UP+RIGHT, buff=0.1)
                arrow_boid = Arrow(start=ORIGIN, end=ORIGIN+RIGHT, buff=0.1)
                arrow_sub = Arrow(start=ORIGIN+RIGHT, end=ORIGIN+UP+RIGHT, buff=0.1)
                arrows = [arrow_vel, arrow_boid, arrow_sub]
                labels = [Text("Avg Position", font_size=12).next_to(arrow_vel, UP),
                                Text("Our Position", font_size=12).next_to(arrow_boid, DOWN),
                                Text("Avg Pos - Our Pos", font_size=12).next_to(arrow_sub, RIGHT)]
                for arrow, label in zip(arrows, labels):
                    self.play(Write(arrow), Write(label))
                    self.wait(3)
                for arrow, label in zip(arrows, labels):
                    self.play(Unwrite(arrow), Unwrite(label))
                self.play(FadeIn(code))
                
            self.wait(w_time)

        
        self.play(Uncreate(code))
        self.wait(2)