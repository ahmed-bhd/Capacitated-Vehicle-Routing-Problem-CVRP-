"""
In Google OR-Tools, a "callback" is a function that the solver calls repeatedly to look up the cost (distance) 
between any two nodes. This keeps the memory footprint low, as the solver only requests values as needed.
"""

# src/cvrp/solvers/distance_callback.py
from typing import List, Callable
from ortools.constraint_solver import pywrapcp

def create_distance_callback(manager: pywrapcp.RoutingIndexManager, distance_matrix: List[List[float]]) -> Callable[[int, int], int]:
    def distance_callback(from_index: int, to_index: int) -> int:
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node])
    
    return distance_callback