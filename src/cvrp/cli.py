"""
This is the orchestrator file. 
It handles data ingestion, dynamic fleet optimization, reporting, and visualization.
"""

import click
import pandas as pd
from pathlib import Path

# Importing project modules
from cvrp.distance.matrix_builder import build_distance_matrix
from cvrp.solvers.ortools_interface import solve_cvrp
from cvrp.routing.solution_extractor import get_routes
from cvrp.routing.route_statistics import get_route_statistics
from cvrp.routing.load_utilization import calculate_capacity_utilization
from cvrp.visualization.color_palette import get_route_colors
from cvrp.visualization.folium_map import generate_interactive_map
from cvrp.reports.fleet_statistics import aggregate_fleet_metrics
from cvrp.reports.summary_report import print_summary_report
from cvrp.reports.csv_exporter import export_routes_to_csv
from cvrp.core.exceptions import CVRPOptimizationError, SolverError

@click.command()
def main():
    # 1. Path Setup
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data" / "locations.csv"
    output_path = current_dir.parent.parent / "output"

    try:
        # Validate data path
        if not data_path.exists():
            raise FileNotFoundError(f"Data file not found at {data_path}")
        
        output_path.mkdir(exist_ok=True)

        # 2. Load and Prepare Data
        click.echo(f"Loading data from: {data_path}")
        df = pd.read_csv(data_path)
        df = df.rename(columns={'latitude': 'lat', 'longitude': 'lon'})
        demands = df['demand'].tolist()
        
        # 3. Dynamic Fleet Configuration
        max_vehicles = 32
        vehicle_capacity = 40
        fixed_cost = 1000345 
        capacities = [vehicle_capacity] * max_vehicles
        
        # 4. Build Model
        click.echo("Building distance matrix...")
        matrix = build_distance_matrix(df, osrm_url="http://localhost:5000")
        
        click.echo(f"Solving CVRP (Max fleet: {max_vehicles})...")
        
        # We call solve_cvrp. Ensure your interface handles the fixed_cost parameter.
        manager, routing, solution = solve_cvrp(
            matrix, demands, capacities, max_vehicles, 0, fixed_cost=fixed_cost
        )
        
        if not solution:
            raise SolverError("The solver could not find a valid solution with current constraints.")

        # 5. Extract and Analyze
        routes = get_routes(manager, routing, solution)
        stats = get_route_statistics(routing, solution, manager)
        utilization = calculate_capacity_utilization(routes, demands, capacities)
        
        # 6. Report and Export
        fleet_metrics = aggregate_fleet_metrics(stats, utilization)
        print_summary_report(fleet_metrics, utilization)
        
        # Save CSV Export
        export_routes_to_csv(routes, output_path)
        
        # 7. Visualization
        colors = get_route_colors(len(routes))
        map_obj = generate_interactive_map(routes, df, colors)
        map_path = output_path / "route_map.html"
        map_obj.save(str(map_path))
        click.echo(f"Map saved to {map_path}")

    except CVRPOptimizationError as e:
        click.echo(f"Optimization Error: {e}")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()















"""
Case 1:
This is the orchestrator file. 
It handles data ingestion, solver execution, reporting, and visualization.
"""


"""
import os
import click
import pandas as pd
from pathlib import Path

# Importing project modules
from cvrp.distance.matrix_builder import build_distance_matrix
from cvrp.solvers.ortools_interface import solve_cvrp
from cvrp.routing.solution_extractor import get_routes
from cvrp.routing.route_statistics import get_route_statistics
from cvrp.routing.load_utilization import calculate_capacity_utilization
from cvrp.visualization.color_palette import get_route_colors
from cvrp.visualization.folium_map import generate_interactive_map
from cvrp.reports.fleet_statistics import aggregate_fleet_metrics
from cvrp.reports.summary_report import print_summary_report
from cvrp.reports.csv_exporter import export_routes_to_csv # Assuming you added this
from cvrp.core.exceptions import CVRPOptimizationError, SolverError

@click.command()
def main():
    # 1. Path Setup
    current_dir = Path(__file__).resolve().parent
    data_path = current_dir / "data" / "locations.csv"
    output_path = current_dir.parent.parent / "output"

    try:
        # Validate data path
        if not data_path.exists():
            raise FileNotFoundError(f"Data file not found at {data_path}")
        
        output_path.mkdir(exist_ok=True)

        # 2. Load and Prepare Data
        click.echo(f"Loading data from: {data_path}")
        df = pd.read_csv(data_path)
        df = df.rename(columns={'latitude': 'lat', 'longitude': 'lon'})
        demands = df['demand'].tolist()
        
        # Configuration
        num_vehicles = 4
        vehicle_capacity = 80
        capacities = [vehicle_capacity] * num_vehicles
        
        # 3. Build model
        click.echo("Building distance matrix...")
        matrix = build_distance_matrix(df, osrm_url="http://localhost:5000")
        
        click.echo("Solving CVRP...")
        manager, routing, solution = solve_cvrp(matrix, demands, capacities, num_vehicles, 0)
        
        if not solution:
            raise SolverError("The solver could not find a valid solution.")

        # 4. Extract and Analyze
        routes = get_routes(manager, routing, solution)
        stats = get_route_statistics(routing, solution, manager)
        utilization = calculate_capacity_utilization(routes, demands, capacities)
        
        # 5. Report and Export
        fleet_metrics = aggregate_fleet_metrics(stats, utilization)
        print_summary_report(fleet_metrics, utilization)
        
        # Save CSV Export
        export_routes_to_csv(routes, output_path)
        
        # Save Map
        colors = get_route_colors(len(routes))
        map_obj = generate_interactive_map(routes, df, colors)
        map_path = output_path / "route_map.html"
        map_obj.save(str(map_path))
        click.echo(f"Map saved to {map_path}")

    except CVRPOptimizationError as e:
        click.echo(f"Optimization Error: {e}")
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

"""