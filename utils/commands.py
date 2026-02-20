"""
Semantic commands used for communication between input, mediator, and game objects.

These commands represent player intentions and high-level game actions,
decoupling input handling from concrete game object behavior.
"""
from enum import auto, Enum


class Command(Enum):
    """
    High-level commands dispatched through the Mediator.

    Each command represents an abstract player action or scene change,
    independent of concrete input devices or key bindings.
    """

    CHANGE_TO_ENTRANCE = auto()
    CHANGE_TO_YARD = auto()
    JUMP = auto()
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    PLAY_JUMP_SOUND = auto()
    RELEASE_TROLLEY = auto()
    STOP = auto()
    TAKE_TROLLEY = auto()
