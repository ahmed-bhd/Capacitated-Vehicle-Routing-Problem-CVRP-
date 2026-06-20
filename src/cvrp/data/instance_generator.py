"""
This module is useful for testing. 
When you don't have real-world OSRM data available or want to perform rapid stress tests, 
this script generates synthetic customer data (random coordinates and demands).
"""

# src/cvrp/data/instance_generator.py
import pandas as pd
import random

def generate_random_instance(num_customers: int, depot_lat: float, depot_lon: float) -> pd.DataFrame:
    """
    Generates a synthetic CVRP instance for testing purposes.
    """
    data = []
    # Add Depot (index 0, demand 0)
    data.append({'id': 'depot', 'lat': depot_lat, 'lon': depot_lon, 'demand': 0})
    
    # Generate random customers
    for i in range(1, num_customers + 1):
        data.append({
            'id': f'cust_{i}',
            'lat': depot_lat + random.uniform(-0.1, 0.1),
            'lon': depot_lon + random.uniform(-0.1, 0.1),
            'demand': random.randint(5, 50)
        })
        
    return pd.DataFrame(data)