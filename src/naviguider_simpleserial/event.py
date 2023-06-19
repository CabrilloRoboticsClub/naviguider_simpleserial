from dataclasses import dataclass


@dataclass
class Event:
    """Base class for events."""

    ticks: int
    """Number of clock ticks since boot."""
