"""
Trolley item implementation for the Piccolo game.
"""
import os
from game_objects.screen import Screen
from utils.constants import (ENTRANCE, FIVE, GRAPHICS_PATH, GROUND_LEVEL, TROLLEY_X)
from utils.helpers import load_image


class Trolley:
    """
    Represents a trolley item in the game.

    Responsibilities:
        - Draw itself on the screen

    Attributes:
        screen: Screen instance for drawing.
        scene_name (str): Name of background where trolley currently is.
        speed (int): Movement speed, used with player input.
        taken (bool): Whether trolley is taken by the player.
        left_trolley_image_normal: Surface for trolley (left-facing) normal size.
        trolley_image_normal: Surface for trolley (right-facing) normal size.
        image: Currently active image surface.
        rect: Pygame rect object for collision detection and determining where the image will be drawn.
    """

    def __init__(self, screen: Screen):
        self.screen = screen
        self.scene_name = ENTRANCE
        self.speed = FIVE
        self.taken = "TODO"

        # Normal (left-facing) images
        self.left_trolley_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "items",
                "trolley_left_empty_normal.png"))

        # Normal (right-facing) images
        self.trolley_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "items",
                "trolley_empty_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.trolley_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom=(TROLLEY_X, GROUND_LEVEL))

    def draw(self) -> None:
        """
        Draw the trolley to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
