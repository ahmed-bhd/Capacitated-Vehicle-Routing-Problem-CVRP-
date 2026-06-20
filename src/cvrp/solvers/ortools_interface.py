"""

Case: 2
To implement the dynamic fleet optimization, we need to add the fixed_cost parameter to your function 
signature and apply it to each vehicle using routing.SetFixedCostOfVehicle().

This is the "engine room" of the project. 
This module initializes the OR-Tools RoutingModel, registers the callbacks, 
adds constraints, and executes the search.
"""
"""
This is the "engine room" of the project. 
This module initializes the OR-Tools RoutingModel, registers the callbacks, 
adds constraints, and executes the search.
"""

from ortools.constraint_solver import pywrapcp
from .distance_callback import create_distance_callback
from .demand_callback import create_demand_callback
from .capacity_dimension import add_capacity_dimension
from .search_parameters import get_search_parameters

def solve_cvrp(distance_matrix, demands, vehicle_capacities, num_vehicles, depot_index, fixed_cost=0):
    """
    Orchestrates the OR-Tools routing model setup and execution.
    """
    # Initialize the Routing Index Manager
    manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot_index)
    routing = pywrapcp.RoutingModel(manager)

    # 1. Register callbacks
    dist_cb = create_distance_callback(manager, distance_matrix)
    dist_cb_index = routing.RegisterTransitCallback(dist_cb)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_cb_index)

    # Demand callback now uses the manager to translate solver indices to node indices
    demand_cb = create_demand_callback(manager, demands)
    demand_cb_index = routing.RegisterUnaryTransitCallback(demand_cb)

    # 2. Add capacity constraint dimension
    add_capacity_dimension(routing, demand_cb_index, vehicle_capacities, num_vehicles)

    # 3. Add Fixed Cost for Dynamic Fleet Sizing
    if fixed_cost > 0:
        for i in range(num_vehicles):
            routing.SetFixedCostOfVehicle(fixed_cost, i)

    # 4. Solve with search parameters
    search_parameters = get_search_parameters()
    solution = routing.SolveWithParameters(search_parameters)
    
    return manager, routing, solution








"""
Case: 1

This is the "engine room" of the project. 
This module initializes the OR-Tools RoutingModel, registers the callbacks, 
adds constraints, and executes the search.
"""
# # src/cvrp/solvers/ortools_interface.py
# from ortools.constraint_solver import pywrapcp
# from .distance_callback import create_distance_callback
# from .demand_callback import create_demand_callback
# from .capacity_dimension import add_capacity_dimension
# from .search_parameters import get_search_parameters

# def solve_cvrp(distance_matrix, demands, vehicle_capacities, num_vehicles, depot_index):
#     """Orchestrates the OR-Tools routing model setup and execution. """
#     # Initialize the Routing Index Manager
#     manager = pywrapcp.RoutingIndexManager(len(distance_matrix), num_vehicles, depot_index)
#     routing = pywrapcp.RoutingModel(manager)

#     # 1. Register callbacks
#     # Distance callback needs the manager to map indices correctly
#     dist_cb = create_distance_callback(manager, distance_matrix)
#     dist_cb_index = routing.RegisterTransitCallback(dist_cb)
#     routing.SetArcCostEvaluatorOfAllVehicles(dist_cb_index)

#     # Demand callback now uses the manager to translate solver indices to node indices
#     demand_cb = create_demand_callback(manager, demands)
#     demand_cb_index = routing.RegisterUnaryTransitCallback(demand_cb)

#     # 2. Add capacity constraint dimension
#     add_capacity_dimension(routing, demand_cb_index, vehicle_capacities, num_vehicles)

#     # 3. Solve with search parameters
#     search_parameters = get_search_parameters()
#     solution = routing.SolveWithParameters(search_parameters)
#     
#     return manager, routing, solution