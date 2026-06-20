"""
This module aggregates data from the individual routes to provide a holistic view of the fleet's performance. 
It calculates fleet-wide metrics such as the total distance covered, the average distance per vehicle, 
and total capacity utilization.
"""

# src/cvrp/reports/fleet_statistics.py
from typing import Dict, List

def aggregate_fleet_metrics(route_stats: Dict, utilization_report: Dict) -> Dict:
    """
    Combines route-specific data into comprehensive fleet-wide statistics.
    """
    total_dist = route_stats["total_distance"]
    active_vehicles = [v for v, s in route_stats.items() 
                       if "Vehicle" in v and s["is_used"]]
    
    return {
        "total_fleet_distance": total_dist,
        "active_vehicle_count": len(active_vehicles),
        "average_distance_per_vehicle": total_dist / len(active_vehicles) if active_vehicles else 0,
        "mean_utilization": sum(utilization_report.values()) / len(utilization_report)
    }

