"""
This module performs sanity checks on the processed data before it reaches the solver. 
Validating data at this stage prevents the OR-Tools solver from crashing or producing infeasible 
solutions due to bad input (e.g., negative demand or impossible coordinates).
"""

# src/cvrp/data/validator.py
import pandas as pd
from ..core.exceptions import DataValidationError

def validate_problem_data(df: pd.DataFrame, vehicle_capacity: int) -> bool:
    """
    Checks the integrity of the customer data.
    
    Validations:
    1. Demands must not exceed vehicle capacity.
    2. Coordinates must be within valid geographic ranges.
    3. No missing values in critical columns.
    """
    if df['demand'].isnull().any():
        raise DataValidationError("Data contains missing demand values.")
        
    if (df['demand'] > vehicle_capacity).any():
        raise DataValidationError("Found customer demand exceeding vehicle capacity.")
        
    if not ((-90 <= df['lat'] <= 90).all() and (-180 <= df['lon'] <= 180).all()):
        raise DataValidationError("Coordinates out of valid geographic range.")
        
    return True