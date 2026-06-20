"""
This module manages the HTTP communication with your OSRM instance. 
It is responsible for sending coordinates to the OSRM "Table" service and parsing the resulting 
JSON travel time/distance matrix.
"""

# src/cvrp/distance/osrm_client.py
import requests
from typing import List, Dict
from ..core.exceptions import OSRMServiceError

def get_osrm_matrix(url: str, coordinates: List[tuple]) -> List[List[float]]:
    """
    Sends coordinates to OSRM and retrieves the distance matrix.
    Coordinates format: [(lon, lat), (lon, lat), ...]
    """
    # OSRM expects lon,lat format
    coord_string = ";".join([f"{c[1]},{c[0]}" for c in coordinates])
    request_url = f"{url}/table/v1/driving/{coord_string}?annotations=distance"
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        data = response.json()
        
        if data['code'] != 'Ok':
            raise OSRMServiceError(f"OSRM Error: {data['message']}")
            
        return data['distances']
    except requests.exceptions.RequestException as e:
        raise OSRMServiceError(f"Failed to connect to OSRM: {e}")