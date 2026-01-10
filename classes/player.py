"""
Player character implementation for the Piccolo game.
"""
import os
from utils.constants import (GRAPHICS_PATH, PLAYER_X, PLAYER_Y)
from utils.helpers import load_image

# Player
class Player:
    """
    Represents the player character (Piccolo) in the game.

    Attributes:
        screen: Screen instance for drawing operations.
        player_x (int): Current X position of the player.
        player_y (int): Current Y position of the player.
        stand_image_normal: Surface for standing animation (right-facing) normal size.
        image: Currently active image surface
        rect: Pygame Rect object for collision detection and determining where the image will be drawn.
    """
    def __init__(self, screen) -> None:
        self.screen = screen
        self.player_x = PLAYER_X
        self.player_y = PLAYER_Y

        # Normal (right-facing) images
        self.stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_stand_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.stand_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom = (self.player_x, self.player_y))

    def draw(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
