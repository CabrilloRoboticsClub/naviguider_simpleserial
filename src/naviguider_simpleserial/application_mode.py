from enum import Enum, auto


class ApplicationMode(Enum):
    """Enum class representing possible application mode values."""

    DRONE = 1
    """Slow merging."""
    SLOW_TARGETING = 2
    """Slow-Medium merging."""
    TARGETING = 3
    """Medium merging."""
    RIFLE = 4
    """Medium-Fast merging."""
    GAMING = 5
    """Fast merging."""
