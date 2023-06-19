from enum import Enum, auto


class CoordinateSystem(Enum):
    """Enum class representing possible coordinate system values."""

    ENU = auto()
    """East, north, up (ENU) coordinate system."""
    NED = auto()
    """North, east, down (NED) coordinate system."""
