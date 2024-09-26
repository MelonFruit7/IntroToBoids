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
        self.play(FadeIn(filesNeeded))


        cur_file = filesNeeded[17:]
        other_files1, other_files1_copy = filesNeeded[:17], filesNeeded[:17].copy()

        self.play(Unwrite(other_files1))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        code = Code("assets/code/realvector.cpp", line_spacing=0.8, font_size=10)
        self.play(DrawBorderThenFill(code[0:2]))
        actual_code = code[2]
        self.play(DrawBorderThenFill(actual_code[0:8]))
        self.wait(3)
        self.play(DrawBorderThenFill(actual_code[9:21]))
        self.wait(1)

        self.ripple(actual_code, range(9, 12), -1)
        self.ripple(actual_code, range(12, 15), -1)
        self.ripple(actual_code, range(15, 18), -1)
        self.ripple(actual_code, range(18, 21), -1)
        self.wait(2)
        self.play(DrawBorderThenFill(actual_code[21:]))
        self.wait(5)

        self.play(Uncreate(code))
        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files1_copy))
        self.wait(2)