from manim import *
import numpy as np

class OptimizedBioNeuralNet(Scene):
    """Performance-optimized version with reduced complexity but enhanced visuals"""
    
    def construct(self):
        # Performance settings
        self.camera.background_color = "#0d1117"
        
        # Streamlined color palette
        self.colors = {
            'input': "#4fc3f7",
            'hidden': "#ff9800", 
            'pathogenic': "#f44336",
            'benign': "#4caf50",
            'synapse': "#64ffda",
            'text': "#e2e8f0"
        }
        
        # Build network efficiently
        self.build_network()
        self.create_labels()
        
        # Execute optimized animations
        self.intro_animation()
        self.forward_propagation()
        self.prediction_result()
    
    def build_network(self):
        """Build network structure with optimized mobject creation"""
        layer_sizes = [4, 6, 2]
        
        # Pre-calculate positions for better performance
        x_positions = [-3, 0, 3]
        y_ranges = [
            np.linspace(-1.5, 1.5, 4),  # Input layer
            np.linspace(-2.5, 2.5, 6),  # Hidden layer  
            np.linspace(-0.5, 0.5, 2)   # Output layer
        ]
        
        # Create nodes efficiently using list comprehension
        self.nodes = []
        for layer_idx, (size, x_pos, y_pos) in enumerate(zip(layer_sizes, x_positions, y_ranges)):
            layer_nodes = []
            for node_idx in range(size):
                node = Circle(
                    radius=0.18,
                    stroke_width=2,
                    stroke_color=WHITE,
                    fill_color=DARK_GRAY,
                    fill_opacity=0.8
                ).move_to([x_pos, y_pos[node_idx], 0])
                layer_nodes.append(node)
            self.nodes.append(layer_nodes)
        
        # Create synapses with batch operations
        self.synapses = []
        for i in range(len(layer_sizes) - 1):
            layer_synapses = []
            for node_in in self.nodes[i]:
                for node_out in self.nodes[i+1]:
                    synapse = Line(
                        node_in.get_right(),
                        node_out.get_left(),
                        stroke_width=1,
                        stroke_opacity=0.3,
                        stroke_color=GRAY
                    )
                    layer_synapses.append(synapse)
            self.synapses.append(layer_synapses)
        
        # Group for efficient operations
        self.all_nodes = VGroup(*[node for layer in self.nodes for node in layer])
        self.all_synapses = VGroup(*[synapse for layer in self.synapses for synapse in layer])
    
    def create_labels(self):
        """Create essential labels only"""
        # Feature labels (simplified)
        features = ["Hydrophobic", "Weight", "Charge", "Position"]
        self.feature_labels = VGroup()
        for i, feature in enumerate(features):
            label = Text(feature, font_size=14, color=self.colors['text']).next_to(
                self.nodes[0][i], LEFT, buff=0.5
            )
            self.feature_labels.add(label)
        
        # Output labels
        self.output_labels = VGroup(
            Text("Pathogenic", font_size=16, color=self.colors['pathogenic']).next_to(
                self.nodes[2][0], RIGHT, buff=0.5
            ),
            Text("Benign", font_size=16, color=self.colors['benign']).next_to(
                self.nodes[2][1], RIGHT, buff=0.5
            )
        )
    
    def intro_animation(self):
        """Streamlined introduction"""
        # Title
        title = Text("Neural Network Prediction", font_size=28, color=self.colors['synapse'])
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(FadeOut(title), run_time=0.8)
        
        # Build network in groups for performance
        self.play(
            AnimationGroup(
                *[DrawBorderThenFill(node) for node in self.all_nodes],
                lag_ratio=0.05
            ),
            run_time=2
        )
        
        self.play(Create(self.all_synapses), run_time=1.5)
        self.play(Write(self.feature_labels), Write(self.output_labels), run_time=1)
        self.wait(0.3)
    
    def forward_propagation(self):
        """Optimized forward propagation animation"""
        # Input activation - batch operation
        input_animations = [
            node.animate.set_fill(self.colors['input'], opacity=0.9)
            for node in self.nodes[0]
        ]
        self.play(*input_animations, run_time=0.8)
        
        # First layer propagation
        synapse_animations = [
            synapse.animate.set_stroke(color=self.colors['synapse'], opacity=0.7, width=2)
            for synapse in self.synapses[0]
        ]
        hidden_animations = [
            node.animate.set_fill(self.colors['hidden'], opacity=0.9)
            for node in self.nodes[1]
        ]
        
        self.play(*synapse_animations, run_time=0.6)
        self.play(*hidden_animations, run_time=0.8)
        
        # Output layer propagation
        output_synapse_animations = [
            synapse.animate.set_stroke(color=self.colors['synapse'], opacity=0.6, width=1.5)
            for synapse in self.synapses[1]
        ]
        self.play(*output_synapse_animations, run_time=0.8)
    
    def prediction_result(self):
        """Final prediction with efficient animations"""
        pathogenic_node = self.nodes[2][0]
        benign_node = self.nodes[2][1]
        
        # Simultaneous result animation
        self.play(
            pathogenic_node.animate.set_fill(self.colors['pathogenic'], opacity=1).scale(1.3),
            benign_node.animate.set_fill(GRAY, opacity=0.3),
            self.output_labels[0].animate.scale(1.2),
            self.output_labels[1].animate.set_opacity(0.4),
            run_time=1.2
        )
        
        # Single flash effect
        self.play(Flash(pathogenic_node, color=self.colors['pathogenic']))
        
        # Result text
        result = Text("PATHOGENIC VARIANT", font_size=24, color=self.colors['pathogenic']).to_edge(UP)
        self.play(Write(result), run_time=1.5)
        
        self.wait(2)
        
        # Clean exit
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)


class InteractiveNeuralNet(Scene):
    """Interactive version with adjustable parameters"""
    
    def construct(self):
        self.camera.background_color = "#0d1117"
        
        # Create control panel
        self.create_controls()
        self.create_network()
        
        # Demo different scenarios
        self.demo_predictions()
    
    def create_controls(self):
        """Create parameter controls"""
        self.controls = VGroup(
            Text("Feature Values:", font_size=18, color=WHITE),
            Text("Hydrophobicity: 0.8", font_size=14),
            Text("Weight: 0.3", font_size=14), 
            Text("Charge: 0.6", font_size=14),
            Text("Position: 0.9", font_size=14)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT)
    
    def create_network(self):
        """Simplified network for interactive demo"""
        # Create minimal viable network
        self.input_nodes = VGroup(*[
            Circle(radius=0.15, color=BLUE).shift(UP * i - UP * 1.5)
            for i in range(4)
        ]).shift(LEFT * 2)
        
        self.output_nodes = VGroup(*[
            Circle(radius=0.15, color=RED if i == 0 else GREEN).shift(UP * i - UP * 0.5)
            for i in range(2)
        ]).shift(RIGHT * 2)
        
        # Simple connections
        self.connections = VGroup(*[
            Line(inp.get_right(), out.get_left(), stroke_width=1, stroke_opacity=0.5)
            for inp in self.input_nodes
            for out in self.output_nodes
        ])
    
    def demo_predictions(self):
        """Demo different prediction scenarios"""
        # Show controls
        self.play(Write(self.controls), run_time=1)
        
        # Show network
        self.play(
            Create(self.input_nodes),
            Create(self.output_nodes), 
            Create(self.connections),
            run_time=1.5
        )
        
        # Demo high-risk case
        self.play(
            self.input_nodes.animate.set_fill(RED, opacity=0.8),
            self.output_nodes[0].animate.set_fill(RED, opacity=1).scale(1.2),
            run_time=1
        )
        
        result_text = Text("HIGH RISK", font_size=24, color=RED).next_to(self.output_nodes, RIGHT)
        self.play(Write(result_text))
        
        self.wait(1.5)
        self.play(FadeOut(result_text))
        
        # Demo low-risk case
        self.play(
            self.controls[1:].animate.set_color(GREEN),
            self.input_nodes.animate.set_fill(GREEN, opacity=0.8),
            self.output_nodes[0].animate.set_fill(GRAY, opacity=0.3).scale(1/1.2),
            self.output_nodes[1].animate.set_fill(GREEN, opacity=1).scale(1.2),
            run_time=1.5
        )
        
        result_text = Text("LOW RISK", font_size=24, color=GREEN).next_to(self.output_nodes, RIGHT)
        self.play(Write(result_text))
        
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
