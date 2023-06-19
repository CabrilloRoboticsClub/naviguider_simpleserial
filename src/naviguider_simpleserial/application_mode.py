from enum import Enum, auto


class ApplicationMode(Enum):
    """Enum class representing possible application mode values."""

    DRONE = auto()
    """Slow merging."""
    GAMING = auto()
    """Fast merging."""
    RIFLE = auto()
    """Medium-Fast merging."""
    SLOW_TARGETING = auto()
    """Slow-Medium merging."""
    TARGETING = auto()
    """Medium merging."""
