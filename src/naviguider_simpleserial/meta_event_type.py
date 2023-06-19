from enum import Enum, auto


class MetaEventType(Enum):
    """Enum class representing possible meta event types."""

    CAL_STATUS_CHANGED = auto()
    """Calibration status has changed."""
    CALIBRATION_STABLE = auto()
    """Calibration is stable."""
    DYNAMIC_RANGE_CHANGED = auto()
    """A sensor's dynamic range has changed."""
    ERROR = auto()
    """A general error has occurred."""
    FIFO_OVERFLOW = auto()
    """The event FIFO has overflowed."""
    FIFO_WATERMARK = auto()
    """The event FIFO is about to overflow."""
    FLUSH_COMPLETE = auto()
    """The event FIFO has been flushed."""
    INITIALIZED = auto()
    """Device initialization has completed."""
    MAGNETIC_TRANSIENT = auto()
    """Magnetic transient has been detected."""
    POWER_MODE_CHANGED = auto()
    """A sensor's power mode has changed."""
    SAMPLE_RATE_CHANGED = auto()
    """A sensor's sample rate has changed."""
    SELF_TEST_RESULT = auto()
    """Self-test result is available."""
    SENSOR_ERROR = auto()
    """A sensor error has occurred."""
    STILLNESS_CHANGED = auto()
    """Stillness has changed."""
    TRANSFER_CAUSE = auto()
    """A sensor hardware bus error has occurred."""
