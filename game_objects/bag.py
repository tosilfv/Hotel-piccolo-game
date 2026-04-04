"""
Bag item implementation for the Piccolo game.
"""
import os
from control.mediator import Mediator
from game_objects.screen import Screen
from utils.constants import (BAG_X, ENTRANCE, GRAPHICS_PATH, GROUND_LEVEL)
from utils.helpers import load_image


class Bag:
    """
    Represents a bag item in the game.

    Attributes:
        screen: Screen instance for drawing.
        mediator: Mediator instance for game internal communication.
        scene_name (str): Name of background where bag currently is.
    """

    def __init__(self, screen: Screen, mediator: Mediator | None):
        self.screen = screen
        self.mediator = mediator
        self.scene_name = ENTRANCE

        # Right-facing images
        self.bag_image = load_image(
            os.path.join(GRAPHICS_PATH,
                "items",
                "bag.png"))

        # Set initial surface
        self.image = self.bag_image

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
        # Draw the bag only if it's in the current scene
        if self.mediator and self.scene_name == self.mediator.current_scene:
            self.screen.screen.blit(self.image, self.rect)
