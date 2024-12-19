from .event import Event
from dataclasses import dataclass

@dataclass
class SensorEvent(Event):
    """Base class for sensor events."""

    pass

@dataclass
class AccelerometerSensorEvent(SensorEvent):
    """Event reported when accelerometer sensor data is available."""

    x: float
    """Acceleration force along the x axis (including gravity). in m/s²."""
    y: float
    """Acceleration force along the y axis (including gravity). in m/s²."""
    z: float
    """Acceleration force along the z axis (including gravity). in m/s²."""
    accuracy: float

@dataclass
class GameRotationVectorSensorEvent(SensorEvent):
    """Event reported when game rotation vector sensor data is available."""

    qx: float
    """Rotation vector component along the x axis (x * sin(θ/2))."""
    qy: float
    """Rotation vector component along the y axis (y * sin(θ/2))."""
    qz: float
    """Rotation vector component along the z axis (z * sin(θ/2))."""
    qw: float
    """Scalar component of the rotation vector ((cos(θ/2))."""
    accuracy: float

@dataclass
class GeomagRotationVectorSensorEvent(SensorEvent):
    """Event reported when geo-magnetic rotation vector sensor data is available."""

    qx: float
    """Rotation vector component along the x axis (x * sin(θ/2))."""
    qy: float
    """Rotation vector component along the y axis (y * sin(θ/2))."""
    qz: float
    """Rotation vector component along the z axis (z * sin(θ/2))."""
    qw: float
    """Scalar component of the rotation vector ((cos(θ/2))."""

@dataclass
class GravitySensorEvent(SensorEvent):
    """Event reported when gravity sensor data is available."""

    x: float
    """Force of gravity along the x axis in m/s²."""
    y: float
    """Force of gravity along the y axis in m/s²."""
    z: float
    """Force of gravity along the z axis in m/s²."""
    accuracy: float

@dataclass
class GyroscopeUncalibratedSensorEvent(SensorEvent):
    """Event reported when uncalibrated gyroscope sensor data is available."""

    x: float
    """Rate of rotation (without drift compensation) around the x axis in rad/s"""
    y: float
    """Rate of rotation (without drift compensation) around the y axis in rad/s"""
    z: float
    """Rate of rotation (without drift compensation) around the z axis in rad/s"""
    bias_x: float
    """Estimated drift around the x axis in rad/s"""
    bias_y: float
    """Estimated drift around the y axis in rad/s"""
    bias_z: float
    """Estimated drift around the z axis in rad/s"""
    accuracy: float

@dataclass
class GyroscopeSensorEvent(SensorEvent):
    """Event reported when uncalibrated gyroscope sensor data is available."""

    x: float
    """Rate of rotation around the x axis in rad/s"""
    y: float
    """Rate of rotation around the y axis in rad/s"""
    z: float
    """Rate of rotation around the z axis in rad/s"""
    accuracy: float

@dataclass
class LinearAccelerationSensorEvent(SensorEvent):
    """Event reported when linear acceleration sensor data is available."""

    x: float
    """Acceleration force along the x axis (excluding gravity) in m/s²."""
    y: float
    """Acceleration force along the y axis (excluding gravity) in m/s²."""
    z: float
    """Acceleration force along the z axis (excluding gravity) in m/s²."""
    accuracy: float

@dataclass
class MagnetometerUncalibratedSensorEvent(SensorEvent):
    x: float
    """Geomagnetic field strength (without hard iron calibration) along the x axis in micro-Tesla (µT)."""
    y: float
    """Geomagnetic field strength (without hard iron calibration) along the y axis in micro-Tesla (µT)."""
    z: float
    """Geomagnetic field strength (without hard iron calibration) along the z axis in micro-Tesla (µT)."""
    offset_x: float
    """Iron bias estimation along the x axis in micro-Tesla (µT)."""
    offset_y: float
    """Iron bias estimation along the y axis in micro-Tesla (µT)."""
    offset_z: float
    """Iron bias estimation along the z axis in micro-Tesla (µT)."""
    accuracy: float

@dataclass
class MagnetometerSensorEvent(SensorEvent):
    """Event reported when magnetometer data is available."""

    x: float
    """Geomagnetic field strength along the x axis in micro-Tesla (µT)."""
    y: float
    """Geomagnetic field strength along the y axis in micro-Tesla (µT)."""
    z: float
    """Geomagnetic field strength along the z axis in micro-Tesla (µT)."""
    accuracy: float

@dataclass
class OrientationSensorEvent(SensorEvent):
    """Event reported when orientation sensor data is available."""

    azimuth: float
    """Azimuth (angle around the z-axis) in degrees."""
    pitch: float
    """Pitch (angle around the x-axis) in degrees."""
    roll: float
    """Roll (angle around the y-axis) in degrees."""
    accuracy: float
    """Accuracy value"""

@dataclass
class PressureSensorEvent(SensorEvent):
    """Event reported when pressure sensor data is available."""

    hpa: float
    """Ambient air pressure in hPa."""

@dataclass
class RotationVectorSensorEvent(SensorEvent):
    """Event reported when rotation vector sensor data is available."""

    qx: float
    """Rotation vector component along the x axis (x * sin(θ/2))."""
    qy: float
    """Rotation vector component along the y axis (y * sin(θ/2))."""
    qz: float
    """Rotation vector component along the z axis (z * sin(θ/2))."""
    qw: float
    """Scalar component of the rotation vector ((cos(θ/2))."""
    accuracy: float

@dataclass
class TemperatureSensorEvent(SensorEvent):
    """Event reported when temperature sensor data is available."""

    degrees_celsius: float
    """Device temperature in degrees Celsius (°C)."""
