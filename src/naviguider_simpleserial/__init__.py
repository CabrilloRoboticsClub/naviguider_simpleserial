import re

from .application_mode import ApplicationMode
from .coordinate_system import CoordinateSystem
from .event import Event
from .meta_event import *
from .meta_event_type import MetaEventType
from .mounting_option import MountingOption
from .sensor_event import *
from .sensor_type import SensorType
from .test_result import TestResult
from .wakeup_event import WakeupEvent


def encode_system_restart() -> str:
    """
    Encodes the system restart command to a string.

    :returns: The encoded command string.
    """
    return "X"


def encode_trigger_oneshot_orientation() -> str:
    """
    Encodes the orientation one-shot command to a string.

    :returns: The encoded command string.
    """
    return "O"


def encode_set_mounting_option(mounting_option: MountingOption) -> str:
    """
    Encodes the set mounting option command to a string.

    :param mounting_option: The mounting option to set.

    :returns: The encoded command string.
    """
    return f"M{mounting_option.value}\n"


def encode_set_coordinate_system(coordinate_system: CoordinateSystem) -> str:
    """
    Encodes the set coordinate system command to a string.

    :param coordinate_system: The coordinate system to set.

    :returns: The encoded command string.
    """
    if coordinate_system == CoordinateSystem.ENU:
        return "J4"
    elif coordinate_system == CoordinateSystem.NED:
        return "J3"


def encode_set_meta_event_reporting_off() -> str:
    """
    Encodes the set meta event reporting off command to a string.

    :returns: The encoded command string.
    """
    return "m0"


def encode_set_meta_event_reporting_on() -> str:
    """
    Encodes the set meta event reporting on command to a string.

    :returns: The encoded command string.
    """
    return "m1"


def encode_set_sensor_event_reporting_off() -> str:
    """
    Encodes the set sensor event reporting off command to a string.

    :returns: The encoded command string.
    """
    return "D0"


def encode_set_sensor_event_reporting_on() -> str:
    """
    Encodes the set sensor event reporting on command to a string.

    :returns: The encoded command string.
    """
    return "D1"


def encode_set_verbose_mode_off() -> str:
    """
    Encodes the set verbose mode off command to a string.

    :returns: The encoded command string.
    """
    return "V0"


def encode_set_verbose_mode_on() -> str:
    """
    Encodes the set verbose mode on command to a string.

    :returns: The encoded command string.
    """
    return "V1"


def encode_save() -> str:
    """
    Encodes the save calibration parameters command to a string.

    :returns: The encoded command string.
    """
    return "S"


def encode_set_accelerometer_sensor_rate(rate: float) -> str:
    """
    Encodes the set accelerometer sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s1,{rate}\n"


def encode_set_magnetometer_sensor_rate(rate: float) -> str:
    """
    Encodes the set magnetometer sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s2,{rate}\n"


def encode_set_orientation_sensor_rate(rate: float) -> str:
    """
    Encodes the set orientation sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s3,{rate}\n"


def encode_set_gyroscope_sensor_rate(rate: float) -> str:
    """
    Encodes the set gyroscope sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s4,{rate}\n"


def encode_set_pressure_sensor_rate(rate: float) -> str:
    """
    Encodes the set pressure sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s6,{rate}\n"


def encode_set_temperature_sensor_rate(rate: float) -> str:
    """
    Encodes the set temperature sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s7,{rate}\n"


def encode_set_gravity_sensor_rate(rate: float) -> str:
    """
    Encodes the set gravity sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s9,{rate}\n"


def encode_set_linear_acceleration_sensor_rate(rate: float) -> str:
    """
    Encodes the set linear acceleration sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s10,{rate}\n"


def encode_set_rotation_vector_sensor_rate(rate: float) -> str:
    """
    Encodes the set rotation vector sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s11,{rate}\n"


def encode_set_magnetometer_uncalibrated_sensor_rate(rate: float) -> str:
    """
    Encodes the set magnetometer uncalibrated sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s14,{rate}\n"


def encode_set_game_rotation_vector_sensor_rate(rate: float) -> str:
    """
    Encodes the set game rotation vector sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s15,{rate}\n"


def encode_set_gyroscope_uncalibrated_sensor_rate(rate: float) -> str:
    """
    Encodes the set gyroscope uncalibrated sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s16,{rate}\n"


def encode_set_geomag_rotation_vector_sensor_rate(rate: float) -> str:
    """
    Encodes the set geo-magnetic rotation vector sensor command to a string.

    :param rate: The desired output data rate in Hz.

    :returns: The encoded command string.
    """
    return f"s20,{rate}\n"


def encode_power_down() -> str:
    """
    Encodes the power down command to a string.

    :returns: The encoded command string.
    """
    return "P"


def encode_autocal_start() -> str:
    """
    Encodes the autocal start command to a string.

    :returns: The encoded command string.
    """
    return "J0"


def encode_autocal_stop() -> str:
    """
    Encodes the autocal stop command to a string.

    :returns: The encoded command string.
    """
    return "J1"


def encode_set_application_mode(application_mode: ApplicationMode) -> str:
    """
    Encodes the set application mode command to a string.

    :param application_mode: The application mode to set.

    :returns: The encoded command string.
    """
    return f"A{application_mode.value}\n"


def encode_set_custom_application_mode(
    overall_merge: float,
    mag_merge: float,
    accel_merge: float,
    dynamic_accel: int,
    still_delay: int,
) -> str:
    """
    Encodes the set custom application mode command to a string.

    :param overall_merge: The overall merge rate to use.
    :param mag_merge: The mag merge rate to use.
    :param accel_merge: The accel merge rate to use.
    :dynamic accel: The dynamic accel value to use.
    :still_delay: The still delay value to use.

    :returns: The encoded command string.
    """
    return f"A0\n{overall_merge:f}\n{mag_merge:f}\n{accel_merge:f}\n{dynamic_accel:d}\n{still_delay:d}\n"


def encode_self_test() -> str:
    """
    Encodes the self-test command to a string.

    :returns: The encoded command string.
    """
    return "B"


def decode_line(line: str) -> Event:
    """
    Decodes a response string to an event.

    :param line: The response string to decode.

    :returns: A decoded event.
    """
    fields = line.split(", ")
    if re.match(r"^[0-9]+$", fields[0]):
        ticks = int(fields[0])
        return decode_event(ticks, fields[1:])


def decode_event(ticks: int, fields: list[str]) -> Event:
    """
    Decodes response fields to an Event.

    :param ticks: The decoded ticks value.
    :param fields: The fields to decode.

    :returns: The decoded Event.
    """
    if fields[0] == "wakeup":
        return decode_wakeup_event(ticks, fields[1:])
    elif fields[0] == "meta event":
        return decode_meta_event(ticks, fields[1:])
    else:
        return decode_sensor_event(ticks, fields)


def decode_wakeup_event(ticks: int, fields: list[str]) -> WakeupEvent:
    """
    Decodes response fields to a WakeupEvent.

    :param ticks: The decoded ticks value.
    :param fields: The fields to decode.

    :returns: The decoded WakeupEvent.
    """
    return WakeupEvent(ticks)


def decode_meta_event(ticks: int, fields: list[str]) -> MetaEvent:
    """
    Decodes response fields to a MetaEvent.

    :param ticks: The decoded ticks value.
    :param fields: The fields to decode.

    :returns: The decoded MetaEvent.
    """
    meta_event_type = decode_meta_event_type(fields[0])
    if meta_event_type == MetaEventType.SAMPLE_RATE_CHANGED:
        return SampleRateChangedMetaEvent(ticks, _decode_sensor_type(fields[1]))
    elif meta_event_type == MetaEventType.POWER_MODE_CHANGED:
        return PowerModeChangedMetaEvent(ticks, _decode_sensor_type(fields[1]))
    elif meta_event_type == MetaEventType.ERROR:
        return ErrorMetaEvent(ticks, int(fields[1]), int(fields[2]))
    elif meta_event_type == MetaEventType.MAGNETIC_TRANSIENT:
        return MagTransientMetaEvent(ticks, fields[1] == "1")
    elif meta_event_type == MetaEventType.CAL_STATUS_CHANGED:
        return CalStatusChangedMetaEvent(ticks, int(fields[1]), int(fields[2]))
    elif meta_event_type == MetaEventType.STILLNESS_CHANGED:
        return StillnessChangedMetaEvent(ticks, fields[1] == "1")
    elif meta_event_type == MetaEventType.CALIBRATION_STABLE:
        return CalibrationStableMetaEvent(ticks, fields[1] == "1")
    elif meta_event_type == MetaEventType.SENSOR_ERROR:
        return SensorErrorMetaEvent(
            ticks, _decode_sensor_type(fields[1]), int(fields[2])
        )
    elif meta_event_type == MetaEventType.FIFO_OVERFLOW:
        return FifoOverflowMetaEvent(ticks, (int(fields[2]) << 8) | int(fields[1]))
    elif meta_event_type == MetaEventType.DYNAMIC_RANGE_CHANGED:
        return DynamicRangeChangedMetaEvent(ticks, _decode_sensor_type(fields[1]))
    elif meta_event_type == MetaEventType.FIFO_WATERMARK:
        return FifoWatermarkMetaEvent(ticks, int(fields[1]))
    elif meta_event_type == MetaEventType.SELF_TEST_RESULT:
        return SelfTestResultMetaEvent(
            ticks,
            _decode_sensor_type(fields[1]),
            decode_test_result_value(fields[2]),
        )
    elif meta_event_type == MetaEventType.INITIALIZED:
        return InitializedMetaEvent(ticks, (int(fields[2]) << 8) | int(fields[1]))
    elif meta_event_type == MetaEventType.TRANSFER_CAUSE:
        return TransferCauseMetaEvent(ticks)
    else:
        print(f"unknown meta event: fields = {fields}")


def decode_meta_event_type(meta_event_type: str) -> MetaEventType:
    """
    Decodes a meta event type name or id string to a MetaEventType enum value.

    :param meta_event_string: The meta event tu[e name or id string to decode.

    :returns: The decoded MetaEvent enum value.
    """
    if meta_event_type in ["Flush Complete", 1]:
        return MetaEventType.FLUSH_COMPLETE
    elif meta_event_type in ["Sample Rate Changed", 2]:
        return MetaEventType.SAMPLE_RATE_CHANGED
    elif meta_event_type in ["Power Mode Changed", 3]:
        return MetaEventType.POWER_MODE_CHANGED
    elif meta_event_type in ["Error", 4]:
        return MetaEventType.ERROR
    elif meta_event_type in ["Mag Transient", 5]:
        return MetaEventType.MAGNETIC_TRANSIENT
    elif meta_event_type in ["Cal Status Changed", 6]:
        return MetaEventType.CAL_STATUS_CHANGED
    elif meta_event_type in ["Stillness Changed", 7]:
        return MetaEventType.STILLNESS_CHANGED
    elif meta_event_type in ["Calibration Stable", 9]:
        return MetaEventType.CALIBRATION_STABLE
    elif meta_event_type in ["Sensor Error", 11]:
        return MetaEventType.SENSOR_ERROR
    elif meta_event_type in ["Fifo overflow", 12]:
        return MetaEventType.FIFO_OVERFLOW
    elif meta_event_type in ["Dynamic Range Changed", 13]:
        return MetaEventType.DYNAMIC_RANGE_CHANGED
    elif meta_event_type in ["Fifo Watermark", 14]:
        return MetaEventType.FIFO_WATERMARK
    elif meta_event_type in ["Self-Test Result", 15]:
        return MetaEventType.SELF_TEST_RESULT
    elif meta_event_type in ["Initialized", 16]:
        return MetaEventType.INITIALIZED
    elif meta_event_type in ["Transfer Cause", 17]:
        return MetaEventType.TRANSFER_CAUSE


def decode_test_result_value(test_result_value: str) -> TestResult:
    """
    Decodes a test result name or id string to a TestResult enum value.

    :param test_result_string: The test result name or id string to decode.

    :returns: The decoded TestResult enum value.
    """
    if test_result_value in ["Test Passed", 0]:
        return TestResult.PASSED
    elif test_result_value in ["X Axis Failed", 1]:
        return TestResult.X_FAILED
    elif test_result_value in ["Y Axis Failed", 2]:
        return TestResult.Y_FAILED
    elif test_result_value in ["X & Y Axes Failed", 3]:
        return TestResult.XY_FAILED
    elif test_result_value in ["z Axis Failed", 4]:
        return TestResult.Z_FAILED
    elif test_result_value in ["X & Z Axes Failed", 5]:
        return TestResult.XZ_FAILED
    elif test_result_value in ["Y & Z Axes Failed", 6]:
        return TestResult.YZ_FAILED
    elif test_result_value in [
        "All Axis Failed or Single Test Failed(no axis test)",
        7,
    ]:
        return TestResult.XYZ_FAILED


def decode_sensor_event(ticks: int, fields: list[str]) -> SensorEvent:
    """
    Decodes response fields to a SensorEvent.

    :param ticks: The decoded ticks value.
    :param fields: The fields to decode.

    :returns: The decoded SensorEvent.
    """
    sensor = _decode_sensor_type(fields[0])
    values = [float(x) for x in fields[1:]]
    if sensor == SensorType.ACCELEROMETER:
        return AccelerometerSensorEvent(ticks, *values)
    elif sensor == SensorType.MAGNETOMETER:
        return MagnetometerSensorEvent(ticks, *values)
    elif sensor == SensorType.GYROSCOPE:
        return GyroscopeSensorEvent(ticks, *values)
    elif sensor == SensorType.ORIENTATION:
        return OrientationSensorEvent(ticks, *values)
    elif sensor == SensorType.PRESSURE:
        return PressureSensorEvent(ticks, *values)
    elif sensor == SensorType.TEMPERATURE:
        return TemperatureSensorEvent(ticks, *values)
    elif sensor == SensorType.GRAVITY:
        return GravitySensorEvent(ticks, *values)
    elif sensor == SensorType.LINEAR_ACCELERATION:
        return LinearAccelerationSensorEvent(ticks, *values)
    elif sensor == SensorType.ROTATION_VECTOR:
        return RotationVectorSensorEvent(ticks, *values)
    elif sensor == SensorType.MAGNETOMETER_UNCALIBRATED:
        return MagnetometerUncalibratedSensorEvent(ticks, *values)
    elif sensor == SensorType.GAME_ROTATION_VECTOR:
        return GameRotationVectorSensorEvent(ticks, *values)
    elif sensor == SensorType.GYROSCOPE_UNCALIBRATED:
        return GyroscopeUncalibratedSensorEvent(ticks, *values)
    elif sensor == SensorType.GEOMAG_ROTATION_VECTOR:
        return GeomagRotationVectorSensorEvent(ticks, *values)
    else:
        print(f"unknown sensor event: fields = {fields}")


def _decode_sensor_type(sensor_type: str) -> SensorType:
    """
    Decodes a sensor type name or id string to a SensorType enum value.

    :param sensor_event_string: The sensor event name or id string to decode.

    :returns: The decoded SensorType enum value.
    """
    if sensor_type in ["accelerometer", "1"]:
        return SensorType.ACCELEROMETER
    elif sensor_type in ["magnetic field", "2"]:
        return SensorType.MAGNETOMETER
    elif sensor_type in ["Orientation", "3"]:
        return SensorType.ORIENTATION
    elif sensor_type in ["gyroscope", "4"]:
        return SensorType.GYROSCOPE
    elif sensor_type in ["pressure", "6"]:
        return SensorType.PRESSURE
    elif sensor_type in ["temperature", "7"]:
        return SensorType.TEMPERATURE
    elif sensor_type in ["gravity", "9"]:
        return SensorType.GRAVITY
    elif sensor_type in ["linear acceleration", "10"]:
        return SensorType.LINEAR_ACCELERATION
    elif sensor_type in ["rotation vector", "11"]:
        return SensorType.ROTATION_VECTOR
    elif sensor_type in ["magnetic field uncalibrated", "14"]:
        return SensorType.MAGNETOMETER_UNCALIBRATED
    elif sensor_type in ["game rotation vector", "15"]:
        return SensorType.GAME_ROTATION_VECTOR
    elif sensor_type in ["gyroscope uncalibrated", "16"]:
        return SensorType.GYROSCOPE_UNCALIBRATED
    elif sensor_type in ["geomagnetic rotation vector", "20"]:
        return SensorType.GEOMAG_ROTATION_VECTOR
