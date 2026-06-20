"""
Before putting routes on a map, we need to convert your list of node indices into a list of geographic coordinates 
(lat, lon) that mapping libraries like Folium can understand.
"""

# src/cvrp/visualization/route_polylines.py
import pandas as pd
from typing import List

def build_route_coordinates(route: List[int], df: pd.DataFrame) -> List[tuple]:
    """
    Maps list of node indices to (lat, lon) coordinates from the dataframe.
    """
    coords = []
    for node_index in route:
        # Extract lat/lon for the row where 'id' matches node_index
        # Assuming df has an 'id' column or index corresponds to df order
        row = df.iloc[node_index]
        coords.append((row['lat'], row['lon']))
    return coords

