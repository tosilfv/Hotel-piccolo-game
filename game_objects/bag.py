"""
Bag item implementation for the Piccolo game.
"""
import os
from control.mediator import Mediator
from game_objects.screen import Screen
from utils.constants import (BAG_X, GRAPHICS_PATH, GROUND_LEVEL)
from utils.helpers import load_image


class Bag:
    """
    Represents a bag item in the game.

    Attributes:
        screen: Screen instance for drawing.
        mediator: Mediator instance for game internal communication.
    """

    def __init__(self, screen: Screen, mediator: Mediator | None):
        self.screen = screen
        self.mediator = mediator

        # Normal (right-facing) images
        self.bag_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "items",
                "bag_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.bag_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom=(BAG_X, GROUND_LEVEL))

    def update(self) -> None:
        """
        Update bag position on every frame.
        """
        pass

    def draw(self) -> None:
        """
        Draw the bag to the screen.
        """
        pass
