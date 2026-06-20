"""
This module handles the ingestion of raw data (e.g., from CSV files) and converts it into structured 
formats that the solver can utilize.
"""

# src/cvrp/data/input_parser.py
import pandas as pd
from typing import Dict, Any
from ..core.exceptions import DataValidationError

def load_customer_data(file_path: str) -> pd.DataFrame:
    """
    Loads customer data from a CSV file.
    Expected columns: 'id', 'lat', 'lon', 'demand'.
    """
    try:
        df = pd.read_csv(file_path)
        required_cols = {'id', 'lat', 'lon', 'demand'}
        if not required_cols.issubset(df.columns):
            raise DataValidationError(f"Missing required columns. Expected: {required_cols}")
        return df
    except Exception as e:
        raise DataValidationError(f"Error reading CSV file: {e}")

def parse_config_to_dict(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parses raw configuration dictionary into validated model parameters.
    """
    # Define schema for required parameters
    try:
        return {
            "num_vehicles": int(config.get("default_vehicle_capacity", 100)),
            "depot_index": int(config.get("depot_index", 0)),
            "time_limit": float(config.get("time_limit_seconds", 30.0)),
            "first_solution": config.get("first_solution_strategy", "PATH_CHEAPEST_ARC"),
            "metaheuristic": config.get("local_search_metaheuristic", "GUIDED_LOCAL_SEARCH")
        }
    except (TypeError, ValueError) as e:
        raise DataValidationError(f"Invalid configuration format: {e}")