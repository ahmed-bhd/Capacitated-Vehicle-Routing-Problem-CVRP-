"""
To make your maps readable, you need a way to assign unique colors to each vehicle's route. 
This module manages a color palette so that when you plot multiple routes on a map, the viewer can easily 
distinguish which path belongs to which vehicle.
"""

# src/cvrp/visualization/color_palette.py
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def get_route_colors(num_vehicles: int) -> list:
    """
    Generates a list of distinct hex colors for a given number of vehicles.
    """
    # Use the 'tab20' colormap for high-contrast, distinct colors
    cmap = cm.get_cmap('tab20', num_vehicles)
    return [mcolors.to_hex(cmap(i)) for i in range(num_vehicles)]
