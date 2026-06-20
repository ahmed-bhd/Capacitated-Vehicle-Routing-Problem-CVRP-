"""
This is a special Pytest file used for "fixtures"—reusable bits of data or setup routines that your tests share. 
Instead of defining a mock distance_matrix in every single test file, you define it once here.
"""

# tests/conftest.py
import pytest
from cvrp.core.type_aliases import Matrix

@pytest.fixture
def mock_distance_matrix() -> Matrix:
    """Provides a sample 3x3 distance matrix for testing."""
    return [
        [0, 10, 20],
        [10, 0, 15],
        [20, 15, 0]
    ]