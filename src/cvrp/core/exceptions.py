"""
This module defines custom exceptions for the project. 
Using custom exceptions allows the application to handle specific failure 
modes (e.g., OSRM server unreachable, invalid data) gracefully and provide meaningful error 
messages to the user.
"""

# src/cvrp/core/exceptions.py

class CVRPOptimizationError(Exception):
    """Base exception class for all custom project errors."""
    pass

class DataValidationError(CVRPOptimizationError):
    """Raised when input data is malformed."""
    def __init__(self, message="Invalid input data detected."):
        super().__init__(message)

class OSRMServiceError(CVRPOptimizationError):
    """Raised when the routing engine is unreachable."""
    def __init__(self, message="OSRM service is unavailable."):
        super().__init__(message)

class SolverError(CVRPOptimizationError):
    """Raised when the OR-Tools solver returns no solution."""
    pass