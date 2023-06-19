from enum import Enum, auto


class TestResult(Enum):
    """Enum class representing possible test result values."""

    PASSED = 0
    """All axes passed."""
    X_FAILED = 1
    """X axis failed."""
    Y_FAILED = 2
    """Y axis failed."""
    XY_FAILED = 3
    """X and Y axes failed."""
    Z_FAILED = 4
    """Z axis failed."""
    XZ_FAILED = 5
    """X and Z axes failed."""
    YZ_FAILED = 6
    """Y and Z axes failed."""
    XYZ_FAILED = 7
    """All axes failed."""
