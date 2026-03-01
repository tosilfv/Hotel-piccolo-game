"""
Bag item implementation for the Piccolo game.
"""
from control.mediator import Mediator
from game_objects.screen import Screen


class Bag:
    """
    Represents a bag item in the game.
    """

    def __init__(self, screen: Screen, mediator: Mediator | None):
        self.screen = screen
        self.mediator = mediator

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass
