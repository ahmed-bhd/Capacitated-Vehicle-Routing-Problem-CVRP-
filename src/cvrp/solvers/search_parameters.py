"""
Assuming we have your environment fixed, we proceed to configure the search parameters. 
This module defines how the solver searches for a solution (e.g., should it try to be fast, 
or should it try to find the absolute best path?).
"""

# src/cvrp/solvers/search_parameters.py
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def get_search_parameters(time_limit_sec: int = 30) -> pywrapcp.DefaultRoutingSearchParameters:
    """
    Configures the search strategy for the OR-Tools solver.
    """
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    
    # Strategy for finding the initial solution
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    
    # Strategy for improving the solution (Metaheuristic)
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    
    # Limit the time the solver spends searching
    search_parameters.time_limit.seconds = time_limit_sec
    
    return search_parameters