"""
This is the map engine. 
It uses the folium library to generate an interactive HTML map, drawing the polylines we generated 
in the previous step onto a base map centered at your depot.
"""

# src/cvrp/visualization/folium_map.py
import folium
from .route_polylines import build_route_coordinates

def generate_interactive_map(routes, df, colors):
    """
    Generates a Folium map object displaying all optimized routes.
    """
    # Center map on the depot (first node)
    depot = df.iloc[0]
    m = folium.Map(location=[depot['lat'], 
                             depot['lon']], 
                             zoom_start=12)
    
    for i, route in enumerate(routes):
        coords = build_route_coordinates(route, df)
        folium.PolyLine(
            coords, 
            color=colors[i], 
            weight=5, 
            opacity=0.8,
            tooltip=f"Vehicle {i}"
        ).add_to(m)
        
    return m