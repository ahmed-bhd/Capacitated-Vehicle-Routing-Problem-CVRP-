"""
This module serves as the "orchestrator". 
It decides whether to fetch data from the OSRM API or fall back to the Euclidean distance calculation 
(e.g., if the user is offline or the OSRM service is unreachable).
"""

# src/cvrp/distance/matrix_builder.py
import pandas as pd
from typing import List, Optional  # Added Optional
from .osrm_client import get_osrm_matrix
from .fallback_euclidean import calculate_haversine_distance
from ..core.exceptions import OSRMServiceError

def build_distance_matrix(df: pd.DataFrame, osrm_url: Optional[str] = None) -> List[List[float]]:
    """
    Builds a distance matrix. 
    Attempts OSRM first; falls back to Haversine if OSRM fails or is not provided.
    """
    coords = list(zip(df['lat'], df['lon']))
    
    if osrm_url:
        try:
            return get_osrm_matrix(osrm_url, coords)
        except OSRMServiceError:
            print("OSRM call failed, falling back to Haversine calculation.")
            
    # Fallback to Euclidean/Haversine
    n = len(coords)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = calculate_haversine_distance(coords[i], coords[j])
    return matrix

