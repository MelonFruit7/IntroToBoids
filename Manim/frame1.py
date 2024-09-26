from manim import *
import numpy as np

class sc(Scene):
    def construct(self):
        msg = "What are boids?"
        main_text = Text(msg)
        start_of_text = main_text[:7]
        boid_of_text = main_text[7:11]
        end_of_text = main_text[11:]

        self.play(DrawBorderThenFill(main_text))
        self.play(FadeOut(start_of_text, shift=UP*5), FadeOut(end_of_text, shift=UP*5))
        self.play(boid_of_text.animate.center())

        main_text = boid_of_text

        self.play(Transform(main_text, Text("bird-oid object")))
        self.wait(3)

        # Create a circular path
        circular_path = Circle(radius=2)

        self.play(Transform(main_text, Triangle().move_to(circular_path.get_edge_center(RIGHT))))
        self.wait(1)

        # Move the triangle along the path with rotation
        self.play(
            MoveAlongPath(main_text, circular_path, rate_func=linear),
            Rotate(main_text, angle=TAU, about_point=circular_path.get_center(), rate_func=linear),
            run_time=4
        )

        upper_text = Text("Seperation")
        main_image = ImageMobject("assets/separation.png")

        self.play(Transform(main_text, Text("Seperation\nAlignment\nCohesion")))
        self.wait(2)

        self.play(RemoveTextLetterByLetter(main_text, time_per_char=0.05))

        self.play(FadeIn(main_image, time=5), DrawBorderThenFill(upper_text.next_to(main_image, UP)))
        self.wait(4)

        replacement_image = ImageMobject("assets/alignment.png")
        self.play(FadeOut(main_image), FadeIn(replacement_image), Transform(upper_text, Text("Alignment").next_to(main_image, UP)))
        self.wait(4)

        main_image = replacement_image
        replacement_image = ImageMobject("assets/cohesion.png")
        self.play(FadeOut(main_image), FadeIn(replacement_image), Transform(upper_text, Text("Cohesion").next_to(main_image, UP)))
        self.wait(4)

        main_image = replacement_image
        self.play(FadeOut(main_image), FadeOut(upper_text))
        self.wait(2)