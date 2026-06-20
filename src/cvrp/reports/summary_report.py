"""
This is the final output layer. 
It formats the raw dictionary data into a clean, human-readable summary that can be printed to the terminal 
or saved to a log file.
"""

# src/cvrp/reports/summary_report.py

def print_summary_report(fleet_stats: dict, utilization_report: dict):
    """
    Prints a formatted summary of the optimization run.
    """
    print("\n--- CVRP Optimization Report ---")
    print(f"Total Distance: {fleet_stats['total_fleet_distance']:.2f} km")
    print(f"Active Vehicles: {fleet_stats['active_vehicle_count']}")
    print(f"Average Fleet Utilization: {fleet_stats['mean_utilization']:.2f}%")
    
    print("\nVehicle Utilization Breakdown:")
    for vehicle, util in utilization_report.items():
        print(f"  {vehicle}: {util}%")
    print("--------------------------------\n")

