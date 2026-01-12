"""
Player character implementation for the Piccolo game.
"""
import os
from utils.constants import (FIVE, GRAPHICS_PATH, PLAYER_X, PLAYER_Y)
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

        # Normal (right-facing) images
        self.stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_stand_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.stand_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom = (PLAYER_X, PLAYER_Y))

    def move_left(self) -> None:
        """
        Move the player to the left.
        """
        self.rect.x -= FIVE

    def move_right(self) -> None:
        """
        Move the player to the right.
        """
        self.rect.x += FIVE

    def draw(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
