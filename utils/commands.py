from enum import Enum, auto

class Command(Enum):
    MOVE_LEFT = auto()
    MOVE_RIGHT = auto()
    JUMP = auto()
    STOP = auto()
    CHANGE_TO_ENTRANCE = auto()
    CHANGE_TO_YARD = auto()
