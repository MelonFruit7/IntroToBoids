from manim import *

class sc(Scene):
    def construct(self):
        filesNeeded = Text("Boids.cpp\nBoid.cpp\nBoid.hpp\nRealVector.cpp\nRealVector.hpp").scale(0.25).to_edge(UL)
        self.add(filesNeeded)
        self.wait(2)

        boid_header = filesNeeded[17:25]
        realvector_header = filesNeeded[39:]
        other_files1 = filesNeeded[:17].add(filesNeeded[25:39])

        self.play(Unwrite(other_files1))
        self.play(boid_header.animate.center().to_edge(UP).shift(LEFT*2))
        self.play(realvector_header.animate.center().to_edge(UP).shift(RIGHT*2))
        self.wait(4)

        realvector_code = Code("assets/code/realvector.hpp", line_spacing=0.8, font_size=20)[2]
        boid_code = Code("assets/code/boid.hpp", line_spacing=0.8, font_size=20)[2]

        self.play(realvector_header.animate.center().to_edge(UP), FadeOut(boid_header))

        vector_group = VGroup(realvector_header.center().to_edge(UP), realvector_code)
        boid_group = VGroup(boid_header.center().to_edge(UP), boid_code)

        main_sec = realvector_header
        self.play(Transform(main_sec, vector_group))
        self.wait(5)
        self.play(Transform(main_sec, boid_group))
        self.wait(5)
        
        self.play(FadeOut(main_sec))

        self.wait(2)