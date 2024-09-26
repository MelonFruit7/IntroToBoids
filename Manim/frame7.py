from manim import *

class sc(Scene):
    def center_code_around(self, code, line):
        self.play(code.animate.move_to(ORIGIN + DOWN*code[2][line].get_y()))

    def construct(self):
        rec = Rectangle(width=14, height=0.75, color=BLACK, z_index=1).to_edge(UP*0.01)
        rec.set_fill(BLACK, 1)
        self.add(rec)

        filesNeeded = Text("Boids.cpp\nBoid.cpp\nRealVector.cpp").scale(0.25).to_edge(UL)
        self.add(filesNeeded.set_z_index(2))

        cur_file = filesNeeded[0:9]
        other_files = filesNeeded[9:]

        self.play(Unwrite(other_files))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        code = Code("assets/code/mainv2.cpp", line_spacing=0.8, font_size=12, line_no_from=1).next_to(rec, DOWN)
        to_load = [code[2][1:6], code[2][12], code[2][18:20]]
        for chunk in to_load:
            chunk.set_opacity(0)

        self.play(DrawBorderThenFill(code))
        self.wait(2)

        # include statements
        for chunk, w_time in zip(to_load, [4, 8, 2]):
            chunk.set_opacity(1)
            self.play(Write(chunk))
            self.wait(w_time)


        self.play(Uncreate(code))
        self.wait(2)