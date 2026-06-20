"""
This callback allows the solver to look up the demand (load) of each node. 
By translating the internal routing index to the node index, the solver can
accurately track the load as it visits each customer.
"""

# src/cvrp/solvers/demand_callback.py
from typing import List, Callable
from ortools.constraint_solver import pywrapcp

# Ensure the function signature accepts BOTH manager AND demands
def create_demand_callback(manager: pywrapcp.RoutingIndexManager, demands: List[int]) -> Callable[[int], int]:
    def demand_callback(from_index: int) -> int:
        node_index = manager.IndexToNode(from_index)
        return demands[node_index]
    
    return demand_callback