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
        self.add(filesNeeded)

        cur_file = filesNeeded[9:17]
        other_files = filesNeeded[:9].add(filesNeeded[17:])
        other_files_copy = other_files.copy()

        self.play(Unwrite(other_files))
        cur_file_og_position = cur_file.get_center()
        self.play(cur_file.animate.center().to_edge(UP))

        code = Code("assets/code/boid.cpp", line_spacing=0.8, font_size=8)
        self.play(DrawBorderThenFill(code[0:2]))
        actual_code = code[2]

        self.play(DrawBorderThenFill(actual_code[0:13]))
        self.wait(8)
        self.play(DrawBorderThenFill(actual_code[14:20]))
        self.wait(10)

        self.play(DrawBorderThenFill(actual_code[21:39]))
        self.wait(5)
        self.play(code.animate.to_edge(LEFT))