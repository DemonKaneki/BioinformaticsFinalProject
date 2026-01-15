from manim import *

class MutationScanner(Scene):
    def construct(self):
        # 1. Title
        title = Text("Deep-SNP: Mutation Analysis", color=BLUE).to_edge(UP)
        self.play(Write(title))

        # 2. Represent the mutation process
        box = Rectangle(height=2, width=4, color=WHITE)
        mutation_text = Text("Arg → Trp", color=YELLOW).move_to(box.get_center())
        label = Text("Mutation Detected:").next_to(box, UP)
        
        self.play(Create(box), Write(mutation_text), Write(label))
        self.wait(1)

        # 3. Show the "Bio-Deltas" (The features your model sees)
        deltas = VGroup(
            Text("⚖️ Weight: +30.2", color=GREEN).scale(0.7),
            Text("💧 Hydro: -2.7", color=BLUE).scale(0.7),
            Text("⚡ Charge: -1.0", color=ORANGE).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(box, RIGHT, buff=1)

        self.play(Write(deltas), run_time=2)
        self.wait(1)

        # 4. Final Verdict
        verdict_box = RoundedRectangle(corner_radius=0.2, color=RED, fill_opacity=0.3).scale(0.8)
        verdict_text = Text("PATHOGENIC", color=RED).move_to(verdict_box.get_center())
        verdict_group = VGroup(verdict_box, verdict_text).to_edge(DOWN, buff=1.5)

        self.play(FadeIn(verdict_group), Flash(verdict_group, color=RED))
        self.wait(2)