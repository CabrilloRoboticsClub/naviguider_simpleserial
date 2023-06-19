from enum import Enum, auto


class MountingOption(Enum):
    """Enum class representing possible mounting option values."""

    STD_000 = 1
    """Standard mounting."""
    STD_090 = 4
    """-90° heading offset."""
    STD_180 = 5
    """-180° heading offset."""
    STD_270 = 6
    """-270° heading offset."""
    X_UP_000 = 2
    """-90° pitch, 0° heading offset."""
    X_UP_090 = 8
    """-90° pitch, -90° heading offset."""
    X_UP_180 = 9
    """-90° pitch, -180° heading offset."""
    X_UP_270 = 10
    """-90° pitch, -270° heading offset."""
    Y_UP_000 = 3
    """+90° roll, 0° heading offset."""
    Y_UP_090 = 11
    """+90° roll, -90° heading offset."""
    Y_UP_180 = 12
    """+90° roll, -180° heading offset."""
    Y_UP_270 = 13
    """+90° roll, -270° heading offset."""
    Z_DOWN_000 = 7
    """+180° roll, 0° heading offset."""
    Z_DOWN_090 = 14
    """+180° roll, -90° heading offset."""
    Z_DOWN_180 = 15
    """+180° roll, -180° heading offset."""
    Z_DOWN_270 = 16
    """+180° roll, -270° heading offset."""
