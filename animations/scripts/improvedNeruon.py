from manim import *
import numpy as np

class EnhancedBioNeuralNet(Scene):
    def construct(self):
        # Enhanced color palette with gradients and modern look
        self.setup_colors()
        self.setup_camera()
        
        # Create the neural network with improved visuals
        self.create_network_structure()
        self.create_enhanced_labels()
        self.create_data_flow_particles()
        
        # Execute the enhanced animation sequence
        self.animate_network_construction()
        self.animate_data_flow()
        self.animate_prediction_process()
        self.animate_final_verdict()
    
    def setup_colors(self):
        """Define enhanced color scheme with gradients"""
        self.colors = {
            'bg': "#0d1117",
            'input': ["#4fc3f7", "#29b6f6"],  # Blue gradient
            'hidden': ["#ff9800", "#f57c00"],  # Orange gradient
            'output_path': ["#8B7355", "#6B5B47"],  # Muted brown/tan
            'output_benign': ["#5A7C65", "#4A6B56"],  # Muted sage green
            'synapse_inactive': "#2d3748",
            'synapse_active': "#ffd700",
            'text': "#e2e8f0",
            'accent': "#64ffda"
        }
    
    def setup_camera(self):
        """Configure camera for better composition"""
        self.camera.background_color = self.colors['bg']
    
    def create_network_structure(self):
        """Create clean neural network structure like optimized version"""
        layer_sizes = [4, 6, 2]
        
        # Pre-calculate positions for better performance like optimized version
        x_positions = [-3, 0, 3]
        y_ranges = [
            np.linspace(-1.5, 1.5, 4),  # Input layer
            np.linspace(-2.5, 2.5, 6),  # Hidden layer  
            np.linspace(-0.5, 0.5, 2)   # Output layer
        ]
        
        # Create nodes efficiently using list comprehension like optimized version
        self.layers = []
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
            self.layers.append(layer_nodes)
        
        # Create enhanced synapses
        self.create_enhanced_synapses()
    
    def create_enhanced_node(self, layer_idx, node_idx):
        """Create a clean, simple node like the optimized version"""
        base_radius = 0.18
        
        # Simple clean node
        node = Circle(
            radius=base_radius,
            stroke_width=2,
            stroke_color=WHITE,
            fill_color=DARK_GRAY,
            fill_opacity=0.8
        )
        
        return node
    
    def create_enhanced_synapses(self):
        """Create synapses with clean styling like optimized version"""
        self.synapses = []
        
        for i in range(len(self.layers) - 1):
            layer_synapses = []
            for node_in in self.layers[i]:
                for node_out in self.layers[i+1]:
                    synapse = Line(
                        node_in.get_right(),
                        node_out.get_left(),
                        stroke_width=1,
                        stroke_opacity=0.3,
                        stroke_color=self.colors['synapse_inactive']
                    )
                    layer_synapses.append(synapse)
            self.synapses.append(layer_synapses)
        
        # Group for efficient operations like optimized version
        self.all_nodes = VGroup(*[node for layer in self.layers for node in layer])
        self.all_synapses = VGroup(*[synapse for layer in self.synapses for synapse in layer])
    
    def create_enhanced_labels(self):
        """Create clean labels like optimized version"""
        # Simple feature labels
        feature_names = ["Hydrophobic", "Weight", "Charge", "Position"]
        self.feature_labels = VGroup()
        
        for i, name in enumerate(feature_names):
            label = Text(name, font_size=14, color=self.colors['text']).next_to(
                self.layers[0][i], LEFT, buff=0.5
            )
            self.feature_labels.add(label)
        
        # Simple output labels without icons
        self.output_labels = VGroup(
            Text("Pathogenic", font_size=16, color=self.colors['output_path'][0]).next_to(
                self.layers[2][0], RIGHT, buff=0.5
            ),
            Text("Benign", font_size=16, color=self.colors['output_benign'][0]).next_to(
                self.layers[2][1], RIGHT, buff=0.5
            )
        )
    
    def create_data_flow_particles(self):
        """Removed for cleaner animation"""
        pass
    
    def animate_network_construction(self):
        """Clean network construction animation"""
        # Simple title
        title = Text("Neural Network Prediction", font_size=28, color=self.colors['accent'])
        self.add(title)
        self.wait(1)
        self.remove(title)
        
        # Build network cleanly like optimized version
        self.add(
            *[node for layer in self.layers for node in layer]
        )
        
        self.add(*[synapse for layer in self.synapses for synapse in layer])
        self.add(self.feature_labels, self.output_labels)
        
        self.wait(0.5)
    
    def animate_data_flow(self):
        """Clean data flow animation"""
        # Input activation - batch operation like optimized version
        input_animations = [
            node.animate.set_fill(self.colors['input'][0], opacity=0.9)
            for node in self.layers[0]
        ]
        self.play(*input_animations, run_time=0.8)
        
        # First layer propagation
        synapse_animations = [
            synapse.animate.set_stroke(color=self.colors['synapse_active'], opacity=0.7, width=2)
            for synapse in self.synapses[0]
        ]
        hidden_animations = [
            node.animate.set_fill(self.colors['hidden'][0], opacity=0.9)
            for node in self.layers[1]
        ]
        
        self.play(*synapse_animations, run_time=0.6)
        self.play(*hidden_animations, run_time=0.8)
        
        # Output layer propagation
        output_synapse_animations = [
            synapse.animate.set_stroke(color=self.colors['synapse_active'], opacity=0.6, width=1.5)
            for synapse in self.synapses[1]
        ]
        self.play(*output_synapse_animations, run_time=0.8)
    
    def animate_prediction_process(self):
        """Clean prediction process"""
        # Skip probability bars for cleaner look
        pass
    
    def animate_final_verdict(self):
        """Clean final prediction like optimized version"""
        pathogenic_node = self.layers[2][0]
        benign_node = self.layers[2][1]
        
        # Simple highlighting
        self.play(
            pathogenic_node.animate.set_fill(self.colors['output_path'][0], opacity=1).scale(1.3),
            benign_node.animate.set_fill(GRAY, opacity=0.3),
            self.output_labels[0].animate.scale(1.2),
            self.output_labels[1].animate.set_opacity(0.4),
            run_time=1.2
        )
        
        # Simple flash effect
        self.play(Flash(pathogenic_node, color=self.colors['output_path'][0]))
        
        # Simple result text
        result = Text("PATHOGENIC VARIANT", font_size=24, color=self.colors['output_path'][0]).move_to(UP * 2.5)
        self.add(result)
        
        self.wait(2)
        
        # Clean exit
        self.remove(*self.mobjects)
        self.wait(0.5)