from enum import Enum, auto


class TestResult(Enum):
    """Enum class representing possible test result values."""

    PASSED = auto()
    """All axes passed."""
    X_FAILED = auto()
    """X axis failed."""
    Y_FAILED = auto()
    """Y axis failed."""
    XY_FAILED = auto()
    """X and Y axes failed."""
    Z_FAILED = auto()
    """Z axis failed."""
    XZ_FAILED = auto()
    """X and Z axes failed."""
    YZ_FAILED = auto()
    """Y and Z axes failed."""
    XYZ_FAILED = auto()
    """All axes failed."""
