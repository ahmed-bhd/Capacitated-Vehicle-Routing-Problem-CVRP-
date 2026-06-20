"""
This module calculates the performance metrics of the generated routes, 
specifically the total distance traveled and the total load carried per vehicle. 
"""
from ortools.constraint_solver import pywrapcp

def get_route_statistics(routing: pywrapcp.RoutingModel, 
                         solution: pywrapcp.Assignment, 
                         manager: pywrapcp.RoutingIndexManager) -> dict:
    """
    Computes total distance and load for each vehicle.
    A vehicle is 'used' if it visits at least one customer node.
    """
    stats = {}
    total_distance = 0
    
    for vehicle_id in range(routing.vehicles()):
        index = routing.Start(vehicle_id)
        route_dist = 0
        nodes_visited = 0
        
        # Traverse the route
        while not routing.IsEnd(index):
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            
            # Check if this node is not the depot
            if manager.IndexToNode(index) != 0:
                nodes_visited += 1
                
            route_dist += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            
        stats[f"Vehicle_{vehicle_id}"] = {
            "distance": route_dist,
            # A vehicle is used if it visited nodes, regardless of distance
            "is_used": nodes_visited > 0 
        }
        total_distance += route_dist
        
    stats["total_distance"] = total_distance
    return stats