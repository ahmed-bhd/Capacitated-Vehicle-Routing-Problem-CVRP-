"""
This test performs a "smoke test" on the entire system, 
ensuring that the components can pass data to one another correctly.
"""

import pytest
from cvrp.solvers.ortools_interface import solve_cvrp
from cvrp.routing.solution_extractor import get_routes
from cvrp.routing.route_statistics import get_route_statistics

def test_full_optimization_pipeline(mock_distance_matrix):
    """
    Integration test to verify that the pipeline executes 
    from distance matrix input to route statistics output.
    """
    # 1. Setup minimal problem parameters
    demands = [0, 10, 10]
    capacities = [20] 
    num_vehicles = 1
    depot_index = 0

    # 2. Run the solver
    manager, routing, solution = solve_cvrp(
        mock_distance_matrix, 
        demands, 
        capacities, 
        num_vehicles, 
        depot_index
    )

    # 3. Extract Routes
    routes = get_routes(manager, routing, solution)
    
    # 4. Extract Stats
    stats = get_route_statistics(routing, solution, manager)

    # 5. Assertions
    # Ensure a route was actually generated
    assert len(routes) == 1
    assert len(routes[0]) > 0
    
    # Ensure stats are populated
    assert "total_distance" in stats
    assert stats["total_distance"] >= 0
    
    # Verify the vehicle usage - Defensive Assertion
    # Check if the key exists, then check the boolean value
    vehicle_key = "Vehicle_0"
    assert vehicle_key in stats, f"Expected {vehicle_key} in stats: {stats.keys()}"
    assert stats[vehicle_key]["is_used"] is True, f"Vehicle was not marked as used: {stats[vehicle_key]}"