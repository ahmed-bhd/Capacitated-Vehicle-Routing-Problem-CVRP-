import csv

def export_routes_to_csv(routes, output_path):
    """Saves the calculated routes to a CSV file."""
    # Ensure the directory exists
    output_path.mkdir(parents=True, exist_ok=True)
    csv_file = output_path / "optimized_routes.csv"
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Vehicle_ID", "Stop_Sequence", "Node_ID"])
        
        for vehicle_id, route in enumerate(routes):
            for sequence, node_id in enumerate(route):
                writer.writerow([vehicle_id, sequence, node_id])
                
    print(f"Successfully exported routes to: {csv_file}")