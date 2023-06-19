from enum import Enum, auto


class MountingOption(Enum):
    """Enum class representing possible mounting option values."""

    STD_000 = auto()
    """Standard mounting."""
    STD_090 = auto()
    """-90° heading offset."""
    STD_180 = auto()
    """-180° heading offset."""
    STD_270 = auto()
    """-270° heading offset."""
    X_UP_000 = auto()
    """-90° pitch, 0° heading offset."""
    X_UP_090 = auto()
    """-90° pitch, -90° heading offset."""
    X_UP_180 = auto()
    """-90° pitch, -180° heading offset."""
    X_UP_270 = auto()
    """-90° pitch, -270° heading offset."""
    Y_UP_000 = auto()
    """+90° roll, 0° heading offset."""
    Y_UP_090 = auto()
    """+90° roll, -90° heading offset."""
    Y_UP_180 = auto()
    """+90° roll, -180° heading offset."""
    Y_UP_270 = auto()
    """+90° roll, -270° heading offset."""
    Z_DOWN_000 = auto()
    """+180° roll, 0° heading offset."""
    Z_DOWN_090 = auto()
    """+180° roll, -90° heading offset."""
    Z_DOWN_180 = auto()
    """+180° roll, -180° heading offset."""
    Z_DOWN_270 = auto()
    """+180° roll, -270° heading offset."""
