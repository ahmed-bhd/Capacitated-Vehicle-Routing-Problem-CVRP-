"""
This module calculates how efficiently your fleet is being used. 
It measures the "Capacity Utilization," which is the ratio of total demand served versus the total capacity available. 
This helps you identify if you have too many vehicles (under-utilization) or if the vehicles are consistently 
running at maximum capacity (risk of delay).
"""

# src/cvrp/routing/load_utilization.py
from typing import List, Dict

def calculate_capacity_utilization(routes: List[List[int]], 
                                   demands: List[int], 
                                   vehicle_capacities: List[int]) -> Dict[str, float]:
    """
    Calculates the load percentage for each vehicle based on its assigned route.
    """
    utilization_report = {}
    
    for i, route in enumerate(routes):
        # Calculate total load for the current route
        # (Exclude depot nodes 0 at the start and end of the route)
        current_load = sum(demands[node] for node in route if node != 0)
        
        capacity = vehicle_capacities[i]
        utilization = (current_load / capacity) * 100 if capacity > 0 else 0
        
        utilization_report[f"Vehicle_{i}"] = round(utilization, 2)
        
    return utilization_report

