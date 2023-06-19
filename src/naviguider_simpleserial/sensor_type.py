from enum import Enum, auto


class SensorType(Enum):
    """Enum class representing possible sensor types."""

    ACCELEROMETER = auto()
    """Accelerometer sensor."""
    GAME_ROTATION_VECTOR = auto()
    """Game rotation vector sensor."""
    GEOMAG_ROTATION_VECTOR = auto()
    """Geo-magnetic rotation vector sensor."""
    GRAVITY = auto()
    """Gravity sensor."""
    GYROSCOPE = auto()
    """Gyroscope sensor."""
    GYROSCOPE_UNCALIBRATED = auto()
    """Uncalibrated gyroscope sensor."""
    LINEAR_ACCELERATION = auto()
    """Linear acceleration sensor."""
    MAGNETOMETER = auto()
    """Magnetometer sensor."""
    MAGNETOMETER_UNCALIBRATED = auto()
    """Uncalibrated magnetometer sensor."""
    ORIENTATION = auto()
    """Orientation sensor."""
    PRESSURE = auto()
    """Pressure sensor."""
    ROTATION_VECTOR = auto()
    """Rotation vector sensor."""
    SIGNIFICANT_MOTION = auto()
    """Significant motion sensor."""
    TEMPERATURE = auto()
    """Temperature sensor."""
