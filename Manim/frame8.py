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

        code = Code("assets/code/mainv3p1.cpp", line_spacing=0.8, font_size=12, line_no_from=8).next_to(rec, DOWN)
        to_load = [code[2][8:9], code[2][9:14], code[2][0:1], code[2][1:2], code[2][2:7]]
        for chunk in to_load:
            chunk.set_opacity(0)

        self.play(DrawBorderThenFill(code))
        self.wait(2)

        ex_rec = Rectangle(width=4, height=4, color=WHITE)
        ex_lines = VGroup()
        dirs = [[UP, DOWN], [RIGHT, LEFT]]
        for i in range(len(dirs)):
            for a, dir in enumerate(dirs[i]):
                corners = [None, None]
                for b, dir2 in enumerate(dirs[(i+1)%2]):
                    corners[b] = ex_rec.get_corner(dir+dir2) + dirs[i][(a+1) % 2]*0.5
                line_add = Line(corners[0], corners[1], color=RED)
                ex_lines.add(line_add)
                ex_lines.add(Arrow(start=ex_rec.get_edge_center(dir), end=line_add.get_center(), buff=SMALL_BUFF, color=WHITE))

        for i, (chunk, w_time) in enumerate(zip(to_load, [3, 5, 3, 2, 5])):
            chunk.set_opacity(1)
            self.play(Write(chunk))
            if (i == 1):
                self.wait(3)
                self.play(FadeOut(code))
                self.play(Write(ex_rec), Write(ex_lines))
                self.wait(6)
                self.play(Unwrite(ex_rec), Unwrite(ex_lines))
                self.play(FadeIn(code))
            elif (i == 4):
                self.wait(5)
                self.play(FadeOut(code))

                labels = [Text("> max_speed"), Text("/speed"), Text("max_speed/speed")]
                arrow_dirs = [
                    [ORIGIN, ORIGIN+RIGHT+UP],
                    [ORIGIN, ORIGIN+RIGHT*0.1+UP*0.1],
                    [ORIGIN, ORIGIN+RIGHT*0.5+UP*0.5]
                ]

                arrow = Arrow(start=ORIGIN, end=arrow_dirs[0][1], color=WHITE, buff=0)
                self.play(FadeIn(arrow))

                for label, dir in zip(labels, arrow_dirs):
                    self.play(arrow.animate.put_start_and_end_on(dir[0], dir[1]))

                    label.next_to(arrow, UP)
                    self.play(Write(label))
                    self.wait(2)
                    self.play(Unwrite(label))
                self.play(Unwrite(arrow))
                self.play(FadeIn(code))
            self.wait(w_time)
                

        
        self.play(Uncreate(code))
        self.wait(2)