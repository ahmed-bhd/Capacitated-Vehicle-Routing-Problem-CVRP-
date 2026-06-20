"""
This script creates a dummy dataset with coordinates for major German cities.
These locations are spread across the country to create a realistic 
long-haul routing scenario for the OR-Tools solver.
"""

import pandas as pd
import os
from pathlib import Path

def generate_sample_data():
    # 1. Path Setup: Define path relative to THIS script
    # Assumes this script is in: .../src/cvrp/data/generate_sample.py
    script_dir = Path(__file__).resolve().parent
    
    # We want to ensure the file goes into src/cvrp/data/
    data_dir = script_dir
    data_path = data_dir / "locations.csv"
    
    # Create the directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)
    
    # 2. German cities data
    data = {
        'node_id': list(range(12)),
        'name': [
            'Berlin', 'Hamburg', 'Munich', 'Frankfurt', 'Stuttgart', 
            'Düsseldorf', 'Leipzig', 'Dortmund', 'Essen', 'Bremen', 
            'Dresden', 'Hanover'
        ],
        'demand': [0, 25, 30, 20, 25, 20, 15, 25, 20, 30, 15, 20],
        'latitude': [
            52.5200, 53.5511, 48.1351, 50.1109, 48.7758, 
            51.2277, 51.3397, 51.5136, 51.4556, 53.0793, 
            51.0504, 52.3759
        ],
        'longitude': [
            13.4050, 9.9937, 11.5820, 8.6821, 9.1829, 
            6.7735, 12.3731, 7.4653, 7.0116, 8.8017, 
            13.7373, 9.7320
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_csv(data_path, index=False)
    print(f"Successfully generated German logistics data at: {data_path}")

if __name__ == "__main__":
    generate_sample_data()