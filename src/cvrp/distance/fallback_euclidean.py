"""
This module provides a fallback distance calculation based on the Haversine formula (spherical distance). 
It is crucial for robustness: if the OSRM API is down, or if you are working offline, your solver can still 
compute a distance matrix based on straight-line coordinates.
"""

# src/cvrp/distance/fallback_euclidean.py
import math

def calculate_haversine_distance(coord1: tuple, coord2: tuple) -> float:
    """
    Calculates the great-circle distance between two points on the Earth 
    in kilometers using the Haversine formula.
    """
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Earth radius in kilometers
    return 6371 * c