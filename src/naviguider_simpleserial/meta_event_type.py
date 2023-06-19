from enum import Enum, auto


class MetaEventType(Enum):
    """Enum class representing possible meta event types."""

    FLUSH_COMPLETE = 1
    """The event FIFO has been flushed."""
    SAMPLE_RATE_CHANGED = 2
    """A sensor's sample rate has changed."""
    POWER_MODE_CHANGED = 3
    """A sensor's power mode has changed."""
    ERROR = 4
    """A general error has occurred."""
    MAGNETIC_TRANSIENT = 5
    """Magnetic transient has been detected."""
    CAL_STATUS_CHANGED = 6
    """Calibration status has changed."""
    STILLNESS_CHANGED = 7
    """Stillness has changed."""
    CALIBRATION_STABLE = 9
    """Calibration is stable."""
    SENSOR_ERROR = 11
    """A sensor error has occurred."""
    FIFO_OVERFLOW = 12
    """The event FIFO has overflowed."""
    DYNAMIC_RANGE_CHANGED = 13
    """A sensor's dynamic range has changed."""
    FIFO_WATERMARK = 14
    """The event FIFO is about to overflow."""
    SELF_TEST_RESULT = 15
    """Self-test result is available."""
    INITIALIZED = 16
    """Device initialization has completed."""
    TRANSFER_CAUSE = 17
    """A sensor hardware bus error has occurred."""
