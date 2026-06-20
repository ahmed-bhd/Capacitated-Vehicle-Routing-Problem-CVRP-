"""
This module configures the "Dimension" in OR-Tools. 
A dimension is a way to track a cumulative quantity (like capacity) along a route. 
We add the demand callback to this dimension so the solver knows to subtract from the remaining capacity 
as it visits each node.
"""

# src/cvrp/solvers/capacity_dimension.py
from ortools.constraint_solver import routing_enums_pb2, pywrapcp

def add_capacity_dimension(routing: pywrapcp.RoutingModel, 
                           demand_callback_index: int, 
                           vehicle_capacities: list, 
                           num_vehicles: int):
    """
    Adds a capacity dimension to the routing model to track vehicle loads.
    """
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        vehicle_capacities,  # list of capacities per vehicle
        True,  # start cumul to zero
        'Capacity'
    )