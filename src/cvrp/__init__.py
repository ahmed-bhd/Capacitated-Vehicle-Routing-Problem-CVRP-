# src/cvrp/__init__.py
"""
CVRP Optimization Package
Initializes the package and exposes the main functionality.
"""

from .distance.matrix_builder import build_distance_matrix
from .solvers.ortools_interface import solve_cvrp
from .routing.solution_extractor import get_routes
from .routing.route_statistics import get_route_statistics
from .routing.load_utilization import calculate_capacity_utilization
from .visualization.folium_map import generate_interactive_map
from .reports.summary_report import print_summary_report

__all__ = [
    "build_distance_matrix",
    "solve_cvrp",
    "get_routes",
    "get_route_statistics",
    "calculate_capacity_utilization",
    "generate_interactive_map",
    "print_summary_report",
]