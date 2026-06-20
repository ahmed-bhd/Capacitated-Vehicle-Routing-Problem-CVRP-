# src/cvrp/core/type_aliases.py
"""
This file improves code readability by defining reusable type hints 
and project-wide path constants.
"""

from typing import List, Dict, Union, TypeAlias, Tuple
from pathlib import Path

# --- Path Constants ---
# Automatically get the root directory of the project
ROOT_DIR: Path = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Path = ROOT_DIR / "data"
RAW_DATA: Path = DATA_DIR / "raw"
INSTANCE_DIR: Path = DATA_DIR / "instances"

# --- Type Hints ---
# Represent a coordinate point as (latitude, longitude)
Coordinate: TypeAlias = Tuple[float, float]

# Represent a distance/duration matrix as a 2D list of numbers
Matrix: TypeAlias = List[List[Union[float, int]]]

# Represent node data (e.g., demand, coordinates)
NodeData: TypeAlias = Dict[str, Union[float, int, str]]

# Represent a single route as a list of node indices
Route: TypeAlias = List[int]

# Represent the collection of all routes in a solution
Solution: TypeAlias = List[Route]