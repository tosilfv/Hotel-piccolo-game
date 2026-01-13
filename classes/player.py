"""
Player character implementation for the Piccolo game.
"""
import os
from utils.constants import (FIVE, GRAPHICS_PATH, GROUND_LEVEL, PLAYER_X, PLAYER_Y)
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
        self.is_jumping = False
        self.velocity_y = 0
        self.jump_height = -15
        self.gravity = 1
        self.max_height = 200

        # Normal (right-facing) images
        self.stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_stand_normal.png"))

        # Set initial surface (using normal size by default)
        self.image = self.stand_image_normal

        # Set initial rectangle object over surface and place it from midbottom
        self.rect = self.image.get_rect(midbottom = (PLAYER_X, GROUND_LEVEL))

        # Make sure piccolo stands initially at ground level
        self.rect.y = GROUND_LEVEL

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

    def jump(self) -> None:
        """
        The player starts jump.
        """
        if not self.is_jumping:
            self.is_jumping = True

            # Start jump
            self.velocity_y = self.jump_height

    def update(self) -> None:
        """
        Updates player physics on every frame.
        """
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            # Prevent piccolo from going over maximum height
            if self.rect.y <= self.max_height:
                self.rect.y = self.max_height
                self.velocity_y = 0

        # Descending
        if self.rect.y >= GROUND_LEVEL:
            self.rect.y = GROUND_LEVEL
            self.is_jumping = False
            self.velocity_y = 0
        
        # DEBUG
        print(f"Position: {self.rect.y}, Velocity: {self.velocity_y}, Jumping: {self.is_jumping}")

    def draw(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
