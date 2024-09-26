from manim import *

class sc(Scene):
    def construct(self):
        text = Text("Here are the files we'll need")
        filesNeeded = Text("Boids.cpp\nBoid.cpp\nBoid.hpp\nRealVector.cpp\nRealVector.hpp")
        self.play(Write(text))
        self.wait(1)
        self.play(Transform(text, filesNeeded))
        self.wait(5)
        self.play(text.animate.scale(0.25).to_edge(UL))
        self.wait(1)