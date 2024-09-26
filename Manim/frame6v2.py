from manim import *

class sc(Scene):
    def ripple(self, code, lines, time):
        curve = ParametricFunction(lambda t: np.array([0, 0.1 * np.sin(PI * t), 0]), t_range=[0, 1])

        ripples = []

        for line in lines:
            if (len(code[line]) > 0):
                anims = []
                for char in code[line]:
                    curve = curve.copy().move_to(char.get_center() + 0.05 * UP)
                    anims.append(MoveAlongPath(char, curve, run_time=0.5))
                ripples.append(AnimationGroup(anims, lag_ratio=0.1))
        if (time != -1):
            self.play(*ripples, run_time=time)
        else:
            self.play(*ripples)

    def construct(self):
        filesNeeded = Text("Boids.cpp\nBoid.cpp\nRealVector.cpp").scale(0.25).to_edge(UL)

        cur_file = filesNeeded[9:17]
        other_files = filesNeeded[:9].add(filesNeeded[17:])
        other_files_copy = other_files.copy()

        cur_file_og_position = cur_file.get_center()
        self.add(cur_file.center().to_edge(UP))

        code = Code("assets/code/boid.cpp", line_spacing=0.8, font_size=8).to_edge(LEFT)
        self.add(code)
        actual_code = code[2]

        # position 
        dot = Dot(point=3*RIGHT, radius=0.1)
        self.play(DrawBorderThenFill(dot))
        self.wait(2)

        #velocity vector
        vel_vector = Arrow(start=dot.get_center(), end=dot.get_center()+[2, 2, 0], buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.2)
        self.play(DrawBorderThenFill(vel_vector))
        self.wait(6)

        #Scale vector to size
        self.play(vel_vector.animate.put_start_and_end_on(dot.get_center(), dot.get_center() + (vel_vector.get_end() - dot.get_center()) / 2))
        self.ripple(actual_code, range(22, 27), -1)
        self.wait(6)

        opp_vector = Arrow(start=dot.get_center(), end=dot.get_center()+(dot.get_center()-vel_vector.get_end())/2, buff=0, stroke_width=3, max_tip_length_to_length_ratio=0.4)
        self.play(DrawBorderThenFill(opp_vector))
        self.ripple(actual_code, range(28, 29), -1)
        self.wait(6)

        rotation_img = ImageMobject("assets/rotations.webp").scale(0.5).to_edge(DOWN+RIGHT)
        self.play(FadeIn(rotation_img))

        tri_dot_1 = Dot(point=vel_vector.get_end(), radius=0.1, color=RED)
        self.play(Rotate(vel_vector, -PI/2, about_point=dot.get_center()), DrawBorderThenFill(tri_dot_1))
        tri_dot_2 = Dot(point=vel_vector.get_end(), radius=0.1, color=RED)
        self.play(Rotate(vel_vector, -PI, about_point=dot.get_center()), DrawBorderThenFill(tri_dot_2))
        tri_dot_3 = Dot(point=vel_vector.get_end(), radius=0.1, color=RED)
        self.play(Unwrite(vel_vector), DrawBorderThenFill(tri_dot_3))
        self.wait(4)

        tri_dots = VGroup(tri_dot_1, tri_dot_2, tri_dot_3)
        self.play(tri_dots.animate.shift(opp_vector.get_end()-opp_vector.get_start()), Unwrite(opp_vector))
        self.ripple(actual_code, range(30, 36), -1)
        self.wait(4)

        tri_lines_1 = Line(tri_dot_1.get_center(), tri_dot_2.get_center(), 0, color=RED, stroke_width=9)
        tri_lines_2 = Line(tri_dot_2.get_center(), tri_dot_3.get_center(), 0, color=RED, stroke_width=9)
        tri_lines_3 = Line(tri_dot_3.get_center(), tri_dot_1.get_center(), 0, color=RED, stroke_width=9)
        triangle = VGroup(tri_lines_1, tri_lines_2, tri_lines_3)
        self.play(DrawBorderThenFill(triangle))
        self.wait(4)

        self.play(Uncreate(code), Uncreate(triangle), Uncreate(tri_dots), Uncreate(dot), FadeOut(rotation_img))
        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files_copy))
        self.wait(2)