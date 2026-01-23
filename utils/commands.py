"""
Semantic commands used for communication between input, mediator, and game objects.

These commands represent player intentions and high-level game actions,
decoupling input handling from concrete game object behavior.
"""
from enum import Enum, auto


# Command
class Command(Enum):
    """
    High-level commands dispatched through the Mediator.

    Each command represents an abstract player action or scene change,
    independent of concrete input devices or key bindings.
    """
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    JUMP = auto()
    STOP = auto()
    CHANGE_TO_ENTRANCE = auto()
    CHANGE_TO_YARD = auto()
