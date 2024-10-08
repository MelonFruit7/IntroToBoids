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

        code = Code("assets/code/mainv4.cpp", line_spacing=0.8, font_size=10, line_no_from=24).next_to(rec, DOWN)
        to_load = [code[2][1:2] ,code[2][8:9], code[2][10:18], code[2][23:29]]
        for chunk in to_load:
            chunk.set_opacity(0)

        self.play(DrawBorderThenFill(code))
        self.wait(2)

        for i, (chunk, w_time) in enumerate(zip(to_load, [1, 4, 8, 6])):
            chunk.set_opacity(1)
            self.play(Write(chunk))
            self.wait(w_time)

        
        self.play(Uncreate(code))

        code = Code("assets/code/mainv4+.cpp", line_spacing=0.8, font_size=12, line_no_from=7).next_to(rec, DOWN)
        self.play(DrawBorderThenFill(code))
        self.wait(3)
        self.play(Uncreate(code))

        self.wait(2)