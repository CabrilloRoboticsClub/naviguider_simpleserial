from enum import Enum, auto


class SensorType(Enum):
    """Enum class representing possible sensor types."""

    ACCELEROMETER = 1
    """Accelerometer sensor."""
    MAGNETOMETER = 2
    """Magnetometer sensor."""
    ORIENTATION = 3
    """Orientation sensor."""
    GYROSCOPE = 4
    """Gyroscope sensor."""
    PRESSURE = 6
    """Pressure sensor."""
    TEMPERATURE = 7
    """Temperature sensor."""
    GRAVITY = 9
    """Gravity sensor."""
    LINEAR_ACCELERATION = 10
    """Linear acceleration sensor."""
    ROTATION_VECTOR = 11
    """Rotation vector sensor."""
    MAGNETOMETER_UNCALIBRATED = 14
    """Uncalibrated magnetometer sensor."""
    GAME_ROTATION_VECTOR = 15
    """Game rotation vector sensor."""
    GYROSCOPE_UNCALIBRATED = 16
    """Uncalibrated gyroscope sensor."""
    SIGNIFICANT_MOTION = 17
    """Significant motion sensor."""
    GEOMAG_ROTATION_VECTOR = 20
    """Geo-magnetic rotation vector sensor."""
