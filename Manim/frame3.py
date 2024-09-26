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
        filesNeeded = Text("Boids.cpp\nBoid.cpp\nBoid.hpp\nRealVector.cpp\nRealVector.hpp").scale(0.25).to_edge(UL)
        self.add(filesNeeded)
        self.wait(2)

        cur_file = filesNeeded[:9]
        other_files1, other_files1_copy = filesNeeded[9:], filesNeeded[9:].copy()

        self.play(Unwrite(other_files1))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))
        
        self.wait(1)

        code = Code("assets/code/mainv1.cpp", line_spacing=0.8, font_size=20)[2]
        self.play(Write(code))
        self.ripple(code, range(3, 6), -1)
        self.wait(1)
        self.ripple(code, range(7, 14), -1)
        self.wait(1)
        self.ripple(code, range(15, 16), -1)

        self.wait(1)
        self.play(Unwrite(code))

        self.play(cur_file.animate.move_to(cur_file_og_position))
        self.play(Write(other_files1_copy))

        self.wait(2)