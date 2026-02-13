"""
Trolley item implementation for the Piccolo game.
"""
import os
from typing import Tuple
from control.mediator import Mediator
from game_objects.screen import Screen
from utils.constants import (ENTRANCE, FIVE, GRAPHICS_PATH, GROUND_LEVEL,
                             TROLLEY_X)
from utils.helpers import load_image


class Trolley:
    """
    Represents a trolley item in the game.

    Responsibilities:
        - Update internal state based on location and scene name
        - Draw itself on the screen at the correct position

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

    def __init__(self, screen: Screen, mediator: Mediator | None):
        self.screen = screen
        self.mediator = mediator
        self.scene_name = ENTRANCE
        self.speed = FIVE
        self.num_of_bags = "TODO"
        self.taken = False

        # Normal (right-facing) images
        self.trolley_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "items",
                "trolley_empty_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.trolley_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom=(TROLLEY_X, GROUND_LEVEL))

    def update(self, player_pos: Tuple[int, int] | None) -> None:
        """
        Update trolley position on every frame.
        """
        # Trolley is taken
        if player_pos is not None:
            self.rect.midbottom = player_pos

    def draw(self) -> None:
        """
        Draw the trolley to the screen.
        """
        # Draw the trolley only if it's in the current scene or if player is taking it
        if self.mediator and (self.taken or self.scene_name == self.mediator.current_scene):
            self.screen.screen.blit(self.image, self.rect)
