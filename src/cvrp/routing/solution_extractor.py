"""
Once the solver finishes, it returns a cryptic internal object. 
This module is responsible for "extracting" that data into a human-readable format—specifically, 
a list of routes, where each route is a sequence of node indices.
"""

# src/cvrp/routing/solution_extractor.py
from ortools.constraint_solver import pywrapcp

def get_routes(manager: pywrapcp.RoutingIndexManager, 
               routing: pywrapcp.RoutingModel, 
               solution: pywrapcp.Assignment) -> list:
    """
    Parses the solution object into a list of routes.
    """
    routes = []
    for vehicle_id in range(routing.vehicles()):
        index = routing.Start(vehicle_id)
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))  # Add the depot at the end
        routes.append(route)
    return routes