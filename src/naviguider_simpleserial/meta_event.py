from dataclasses import dataclass

from .event import Event
from .sensor_type import SensorType
from .test_result import TestResult


class MetaEvent(Event):
    """Base class for meta events."""

    pass


@dataclass
class CalStatusChangedMetaEvent(MetaEvent):
    """Event reported when calibration status has changed."""

    cal_status: int
    transient: int


@dataclass
class CalibrationStableMetaEvent(MetaEvent):
    """Event reported when calibration is stable."""

    is_stable: bool


@dataclass
class DynamicRangeChangedMetaEvent(MetaEvent):
    """Event reported when the dynamic range for a sensor has changed."""

    sensor_type: SensorType


@dataclass
class ErrorMetaEvent(MetaEvent):
    """Event reported when a general error has occurred."""

    error_register: int
    debug_state: int


@dataclass
class FifoOverflowMetaEvent(MetaEvent):
    """Event reported when the event FIFO has overflowed."""

    loss_count: int


@dataclass
class FifoWatermarkMetaEvent(MetaEvent):
    """Event reported when the event FIFO is about to overflow."""

    bytes_remaining: int


@dataclass
class InitializedMetaEvent(MetaEvent):
    """Event reported when the device has completed initialization."""

    ram_version: int


@dataclass
class MagTransientMetaEvent(MetaEvent):
    """Event reported when magnetic transient has been detected."""

    transient_detected: bool


@dataclass
class PowerModeChangedMetaEvent(MetaEvent):
    """Event reported when the power mode for a sensor has changed."""

    sensor_type: SensorType


@dataclass
class SampleRateChangedMetaEvent(MetaEvent):
    """Event reported when the sample rate for a sensor has changed."""

    sensor_type: SensorType


@dataclass
class SelfTestResultMetaEvent(MetaEvent):
    """Event reported when a self-test result is available."""

    sensor_type: SensorType
    test_result: TestResult


@dataclass
class SensorErrorMetaEvent(MetaEvent):
    """Event reported when a sensor error has occurred."""

    sensor_type: SensorType
    status: int


@dataclass
class StillnessChangedMetaEvent(MetaEvent):
    """Event reported when stillness has changed."""

    is_still: bool


@dataclass
class TransferCauseMetaEvent(MetaEvent):
    """Event reported when a sensor hardware bus error has occurred."""

    pass
