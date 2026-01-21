"""
Player character implementation for the Piccolo game.
"""
import os
from game_objects.screen import Screen
from utils.constants import (FIVE, GRAPHICS_PATH, GRAVITY, GROUND_LEVEL,
                             JUMP_CEILING_Y, JUMP_HEIGHT, PLAYER_X, ZERO)
from utils.helpers import load_image


# Player
class Player:
    """
    Represents the player character (Piccolo) in the game.

    Attributes:
        screen: Screen instance for drawing operations.
        is_jumping (bool): Whether the player is jumping.
        gravity (int): Current gravity of the game.
        jump_height (int): Current Y jump height of the player.
        jump_ceiling_y (int): Maximum height of the player jump.
        velocity_y (int): Current Y velocity of the player.
        stand_image_normal: Surface for standing animation (right-facing) normal size.
        running_images (list): List of piccolo running images for animation (right-facing) normal size.
        running_frame (int): The frame which is either 0 or 1 for running_images list.
        image: Currently active image surface
        rect: Pygame rect object for collision detection and determining where the image will be drawn.
        rect.y: Pygame rect object's Y position.
    """
    
    def __init__(self, screen: Screen) -> None:
        self.screen = screen
        self.is_jumping = False
        self.gravity = GRAVITY
        self.jump_height = JUMP_HEIGHT
        self.jump_ceiling_y = JUMP_CEILING_Y
        self.velocity_y = ZERO

        # Normal (right-facing) images
        self.stand_image_normal = load_image(
            os.path.join(GRAPHICS_PATH,
                "player",
                "piccolo_stand_normal.png"))
        self.running_images = [
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_run1_normal.png")),
            load_image(
                os.path.join(GRAPHICS_PATH,
                    "player",
                    "piccolo_run2_normal.png"))
        ]

        # Set running frame
        self.running_frame = 0

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
        Start player jump.
        """
        if not self.is_jumping:
            self.is_jumping = True

            # Start jump
            self.velocity_y = self.jump_height

    def update(self, running: bool) -> None:
        """
        Update player physics on every frame.
        """
        # Jumping
        if self.is_jumping:
            self.velocity_y += self.gravity
            self.rect.y += self.velocity_y

            # Prevent piccolo from going over maximum height
            if self.rect.y <= self.jump_ceiling_y:
                self.rect.y = self.jump_ceiling_y
                self.velocity_y = 0

        # Descending
        if self.rect.y >= GROUND_LEVEL:
            self.rect.y = GROUND_LEVEL
            self.is_jumping = False
            self.velocity_y = 0
        
        # Running
        if running:
            # Update running frame
            self.running_frame += 1
            # Slow down image change frequency by multiplying
            if self.running_frame >= len(self.running_images) * 10:
                # Reset running frame when all images have been cycled through
                self.running_frame = 0
            # Avoid list index out of range by dividing the frame index
            self.image = self.running_images[self.running_frame // 10]
        
        # Standing
        else:
            # Use standing image when not running
            self.image = self.stand_image_normal
        
        # DEBUG
        # print(f"Position: {self.rect.y}, Velocity: {self.velocity_y}, Jumping: {self.is_jumping}, , Running: {running}")

    def draw(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.screen.blit(self.image, self.rect)
