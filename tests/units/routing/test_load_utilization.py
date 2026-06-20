"""
Example Unit Test (tests/unit/routing/test_load_utilization.py)
This test focuses purely on the math, using the fixture we discussed previously to ensure the calculation is correct 
without needing a real dataset.
"""

# tests/unit/routing/test_load_utilization.py
from cvrp.routing.load_utilization import calculate_capacity_utilization

def test_calculate_capacity_utilization():
    routes = [[0, 1, 2, 0]]
    demands = [0, 50, 50]  # Depot demand is 0
    capacities = [100]
    
    utilization = calculate_capacity_utilization(routes, demands, capacities)
    
    assert utilization["Vehicle_0"] == 100.0

