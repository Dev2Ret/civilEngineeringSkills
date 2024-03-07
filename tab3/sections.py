import plotly.graph_objects as go
import numpy as np
import math

class Sections:
    def __init__(self):
        self.section = 'pipe'

    def pipe(self):
        return

    def angled(self, price):
        return
    
    def rectang(self):
        return
    
    def hBeam(self):
        return

class Hbeam:
    def __init__(self, d, B, tw, tf, R, h, b, n, Lmajor, Lminor, Kmajor, Kminor):
        self.d = d
        self.B = B
        self.tw = tw
        self.tf = tf
        self.R = R
        self.h = h
        self.b = b
        self.n = n
        self.Lmajor = Lmajor
        self.Lminor = Lminor
        self.Kmajor = Kmajor
        self.Kminor = Kminor
        self.visualize_section()

    def calculate_I(self):
        I = (self.B * self.d**3) / 12
        return I

    def calculate_S(self):
        S = (self.B * self.d**2) / 6
        return S
    
    def visualize_section(self):
        # Define points for the flanges and web
        # Assuming symmetrical flanges and web for simplicity
        x_flange_upper = [0, self.B, self.B, 0, 0]
        y_flange_upper = [self.d, self.d, self.d - self.tf, self.d - self.tf, self.d]
        
        x_flange_lower = [0, self.B, self.B, 0, 0]
        y_flange_lower = [0, 0, self.tf, self.tf, 0]
        
        x_web = [self.B/2 - self.tw/2, self.B/2 + self.tw/2, self.B/2 + self.tw/2, self.B/2 - self.tw/2, self.B/2 - self.tw/2]
        y_web = [self.tf, self.tf, self.d - self.tf, self.d - self.tf, self.tf]
        
        # Create Plotly figure
        fig = go.Figure()

        # Add traces for upper flange, web, and lower flange
        fig.add_trace(go.Scatter(x=x_flange_upper, y=y_flange_upper, fill='toself', name='Upper Flange'))
        fig.add_trace(go.Scatter(x=x_web, y=y_web, fill='toself', name='Web'))
        fig.add_trace(go.Scatter(x=x_flange_lower, y=y_flange_lower, fill='toself', name='Lower Flange'))
        
        # Update layout to better represent the section
        fig.update_layout(title='Section Configuration',
                          xaxis_title='Width',
                          yaxis_title='Height',
                          xaxis=dict(range=[0, self.B], scaleanchor="y", scaleratio=1),
                          yaxis=dict(range=[0, self.d], scaleanchor="x", scaleratio=1),
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=False
                          )
        self.fig = fig

        # return fig

class Rectangle:
    def __init__(self, d, B, tw, tf, R=None):
        self.B = B
        self.d = d
        self.tw = tw
        self.tf = tf
        self.R = R
        self.visualize_section()

    # Method to calculate properties like area, moment of inertia, etc.
    def calculate_properties(self):
        return
    
    def visualize_section(self):
        # Define the coordinates for the outer rectangle
        outer_x = [0, self.B, self.B, 0, 0]
        outer_y = [0, 0, self.d, self.d, 0]
        
        # Define the coordinates for the inner rectangle (accounting for thickness)
        inner_x = [self.tw, self.B - self.tw, self.B - self.tw, self.tw, self.tw]
        inner_y = [self.tf, self.tf, self.d - self.tf, self.d - self.tf, self.tf]

        fig = go.Figure()

        # Add the outer rectangle
        fig.add_trace(go.Scatter(x=outer_x, y=outer_y, fill=None, mode='lines', name='Outer Dimensions'))
        
        # Add the inner rectangle
        fig.add_trace(go.Scatter(x=inner_x, y=inner_y, fill='tonexty', mode='lines', name='Inner Dimensions'))
        
        fig.update_layout(title='Rectangular Section with Thickness', 
                          xaxis_title='Width', 
                          yaxis_title='Height',
                          xaxis=dict(scaleanchor="y", scaleratio=1),
                          yaxis=dict(scaleanchor="x", scaleratio=1),
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=False)

        self.fig = fig
        # fig.show()
        # return fig
        

class Pipe:
    def __init__(self, d, t, h=None, n=None, L=None, K=None):
        self.d = d
        self.t = t
        self.visualize_section()

    # Method to calculate properties like area, moment of inertia, etc.
    def calculate_properties(self):
        return

    # Method to visualize the section using Plotly
    def visualize_section(self):
        # Define the outer circle
        outer_theta = np.linspace(0, 2 * np.pi, 100)
        outer_x = (self.d / 2) * np.cos(outer_theta)
        outer_y = (self.d / 2) * np.sin(outer_theta)
        
        # Define the inner circle (subtracting twice the wall thickness from the diameter)
        inner_diameter = self.d - 2 * self.t
        inner_x = (inner_diameter / 2) * np.cos(outer_theta)
        inner_y = (inner_diameter / 2) * np.sin(outer_theta)

        fig = go.Figure()

        # Plot the outer circle
        fig.add_trace(go.Scatter(x=outer_x, y=outer_y, fill=None, mode='lines', name='Outer Diameter'))
        
        # Plot the inner circle
        fig.add_trace(go.Scatter(x=inner_x, y=inner_y, fill='tonexty', mode='lines', name='Inner Diameter'))

        fig.update_layout(title='Pipe Section with Wall Thickness', 
                          xaxis_title='Diameter',
                          yaxis_title='Diameter',
                          xaxis=dict(scaleanchor="y", scaleratio=1),
                          yaxis=dict(scaleanchor="x", scaleratio=1),
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=False)
        self.fig = fig
        # fig.show()
        # return

class Angled:
    def __init__(self, d, b, t):
        self.b = b # Width of on leg
        self.d = d # Height of the other leg
        self.t = t # Thickness
        self.visualize_section()

    def calculate_properties(self):
        return
    
    def visualize_section(self):
        # Assume this is an L-shaped section with equal legs
        fig = go.Figure(data=[
            go.Scatter(x=[0, self.b, self.b, self.b-self.t, self.b-self.t, 0, 0], 
                       y=[0, 0, self.d, self.d, self.t, self.t, 0], 
                       fill='toself')
        ])
        fig.update_layout(title='Angled (L-Shaped) Section', 
                          xaxis_title='Width (b)', 
                          yaxis_title='Height (d)',
                          xaxis=dict(scaleanchor="y", scaleratio=1),
                          yaxis=dict(scaleanchor="x", scaleratio=1),
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=False
                          )
        self.fig = fig
        # fig.show()

# Example usage:
# section = Rectangle(d=300, B=150, tw=10, tf=20, R=0, h=260, b=130, n=0, Lmajor=5000, Lminor=3000, Kmajor=1.0, Kminor=1.0)
# section.plot_section()

# Example usage:
# rect_section_with_thickness = Rectangle(B=200, d=100, tw=10, tf=10)
# rect_section_with_thickness.visualize_section()


# pipe_section = Pipe(d=5, t=0.3)
# pipe_section.visualize_section()

# angle_section = Angled(b=4, d=4, t=0.5)
# angle_section.visualize_section()
